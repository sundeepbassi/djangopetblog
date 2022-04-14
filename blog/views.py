"""This module processes the receiving of web requests and
returns web responses """
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CommentForm
from .models import Post, Comment


def display_about_page(request):
    """ Render the About page """
    return render(request, 'about.html')


def display_gallery_page(request):
    """ Render the Gallery page """
    return render(request, 'gallery.html')


class DisplayAllBlogPosts(generic.ListView):
    """This class lists all the blog posts"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class DisplayBLogPost(View):
    """This class defines the blog post details"""
    def get(self, request, slug, *_args, **_kwargs):
        """Get the blog post details"""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *_args, **_kwargs):
        """Form post of a blog post"""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        # Validate the comment form
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class LikeBlogPost(View):
    """Like a blog post"""
    def post(self, request, slug, *_args, **_kwargs):
        """Remove or add a like, as specified"""
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class UpdateBlogPostComment(SuccessMessageMixin, UpdateView):
    """Update a blog post comment"""
    model = Comment
    template_name = 'update_comment.html'
    success_message = "Your comment was successfully updated."
    fields = ['body']

    # After updating a comment, go to the url specified in this function.
    #
    # Note that this URL, is the page on which we clicked the Edit link,
    # this makes more sense to the user, i.e. they edit (update) a comment
    # on a page then return to that same page, to see the comment updated.
    def get_success_url(self):
        next_url = self.request.GET['nexturl']
        return next_url


class DeleteBlogPostComment(DeleteView):
    """Delete a blog post comment"""
    model = Comment
    template_name = 'delete_comment.html'
    success_message = "Your comment was successfully deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteBlogPostComment,
                     self).delete(request, *args, **kwargs)

    # After deleting a comment, go to the url specified in this function.
    #
    # Note that this URL, is the page on which we clicked the Delete link,
    # this makes more sense to the user, i.e. they delete a comment on a page
    # then return to that same page, to see the comment deleted.
    def get_success_url(self):
        next_url = self.request.GET['nexturl']
        return next_url
