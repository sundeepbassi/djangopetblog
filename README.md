# Introduction
## About Petblog

This blog was created for a user who has an interest in animal welfare and people who loves their pets.

The users name is Stacey for confidentiality purposes the name has been adopted as the user wanted to stay anonymous.  

The background of the user is a single mother staying at home taking care of her children and animals that she has rescued.  The user has always had an interest in taking care of animals and rescuing animals that have been injured.  The user usually uses social media to keep in touch with people that share an interest in animal welfare.

### Initial Discussion
One of the reasons the usere wanted a blog was to create a forum to keep in touch with fellow animal lovers and to also raise awareness about animal welfare. As the user stated "a social media platform for animal lovers and the joy we share in looking after them, our furry companions"




### User Stories


## Strategy

#### Users

### UX

#### Roles

- User

- Potential User

- Managing Site Admin

#### Interestd Users

- Users who have pets and are passionate about animal welfare.

- There is no age range as both adults and children can care for pets.

#### Potential Users

- Then there are those users that are interested in getting a pet and want to learn more about animal welfare.

- During the covid-19 panademic we saw an interest in the number of people wanting to get a pet. Especially as people began to work from home or were furloughed.

- There are also users that for some reason unable to keep a pet (such as the elderly or residential restrictions) and the blog would help them keep in touch by making comments about blog posts.

#### Managing Site Admin
This will be the person who can manage the administration of the site.

### Development Planes

The blog will allow the user to{

  - To see and read posts about pets and animal welfare.

  - To have the opportunity to register and sign up as a user.

  - To be able to leave comments on posts.

  - To be able to update comments that they have left about posts.

  - To be able to delete comments that they have made about posts.

  - If the user gets to the delete stage and wants to cancel deleteing the post they have that option   
    also with the cancel button.

  - The User can also logout.

The blog will allow the admin to:

- Create, read, update and delete posts in the admin section.

- Approve comments made by registered users.

### Scope 

NEED TO LOOK UP SCOPE 


### Structure Check task in figma

## Skeleton

### Wireframes

### Database Schema

### Database Model

### Design

#### Colour 

#### typography

#### Images

### Features

#### Navigation

I decided to keep the main navigation to the left hand side of the user to view as this is where most viewers and users are known to view  awebsite first.  get evidence from ???

#### Header 


#### Footer

#### Home

#### Register

#### Login

#### Update A Comment

#### Delete A Comment

#### Logout





List relevant pages

HOME 

### Future Features

## Technologies Used

### Languages Used
HTML
CSS3
PYTHON
JAVASCRIPT

### Frameworks, Libraries and Programs Used

- [Git]

- [Github]

- Django

- Superuser

- Heroku

- Cloudinary 

### Testing

### Testing User Stories from User Experience (UX) Section

### Further Testing

### Known Bugs

### Known Issues
On the 31st of January I had to contact tutor support again and explain that I could not locate the env.py file that I had created twice on my filing system.  I sent tutor support screen shots of my filess.

Tutor Support informed me that it was best to open up my workspace by gitpod.io/workspaces into your url bar. 

During the deployment process on the 1st of February 2022 there was an error message when opening the app.  Tutor support informed it was best to git commit and push prior to deployment and this resolved the issue and the site was successfully deployed.

On the 1st of February 2022 there were issues with performing the python3 manage.py makemigrations for the data models that were created for the post and comments. The tutors informed me that the issue was to do with Heroku updating its config vars and that I would need to recopy the DATABASE_URL code and put it in the env file.  This resolved the issues and the makemigrations and the migrate commands worked.

On the 2nd of February I noticed that my env.py had disappeared again and I had been working on it the night before to update the config vars links as suggested by the tutors because they informed me that Heroku sometimes update their servers and the links can change.  I contacted the tutors again and informed them that the env.py had disappeared again and I had followed the correct procedures to open the work as suggested by the tutors previously.  I also informed them that I could not log into Heroku.  The tutors told me that the Heroku site was not accessible as engineers were working on it. The tutors helped me to set up a environment variable and told me to use the https://gitpod.io/workspaces to ooen and stop projects.

cloudinary://571451748687539:2KTq0GgqN_vNbGGDB_nWNoN8Lws@sunnyalways

On the 14th of February I had to contact tutor support as I could not make a git commit and I also tried to do it through source control.  I had to do some git commits from the week before.  I had to resubmit my project 3 which took a week to do.  Tutor support said that I would need to do a git pull but the issue was a conflict in the requirements file.  Once this was resolved the tutor support gave me commands to restore my workspace to be able to do git commits.


### Deployment 
The project was deployed early on the 1st of February 2022 as recommended by the Code Institute walkthrough I think therefore I blog. 

Steps to Deployment

- Navigate to the Heroku website

- I already had an account with Heroku

- I Created Petstar app on the Heroku app and selected the location.

- I went to the  resources tab and under add ons typed in Postgres and selected the Postgres Heroku option. Attach the postgreSQL database

- Prepare the  settings.py files and the environment
- I had to click settings tab and clicked on the Reveal Config Vars and from the DATABASE_URL I copied the url next to it.
- Then I had to create a env.py file in the main directory in my Gitpod workspace.

- I added the code to set up the DATABASE_URL in the env.py file. Then I added the value from Heroku next to the Database_URL.

- I set up the SECRET_KEY in the env.py file and also added the value to it.

- Then I went Heroku and in the Config Vars I added the SECRET_KEY value.

- Then I had to update the settings.py file by importing the env.py file and to add the DATABASE_URL and SECRET_KEY file paths.

- Then I had to create an account with Cloudinary.

- From Cloudinary I copied the url and pasted it into the Heroku Config Vars and this was also pasted into the setting.py file. 

- I then went to the settings.py file and added the following sections.

- In the INSTALLED_APPS list I added cloudinary.
- STATICFILE_STORAGE
- STATICFILES_DIRS
- STATIC_ROOT
- MEDIA_URL
- DEFAULT_FILES_STORAGE
- TEMPLATES_DIR
- The DIRS was updated in TEMPLATES WITH TEMPLATES_DIR
- The ALLOWED_HOSTS were updated with ['app_name.heroku.com','localhost']

When I did do the early deployment as advised in the Code Institute wakthrough I think therefoe I blog, the deployment worked good.  Then one day there were problems getting the site to work I had to contact tutor support and they said that because Heroku had been doing maintainance work on their site that Config Vars DATABSE_URL would have been changed and therefore it would be best to recopy this and add it to my env.py file again. I did this and the site worked.

STILL NEED TO ADD MORE INFORMATION
- Get our static and media files stored on cloudinary. 

The final deployment steps

### Credits

On the 28th of January tried to do a number of git commits for what I had done for the project.  I noticed the 29th of January that these commits did not show on my github and I did do a git push also.  Student tutors advised me to ensure that all git commits are done once code has been installed and saved in the files.
The following steps were put into the git commits on the 28th of January. The steps for these installations were shown in the Code Institute Walkthrough project I think therefore I blog.

The layout for the Readme is from Alexander Grib 

[Alexander Grib](https://github.com/alexandergrib/ms4-store)

and

[Irish Becky's readme](https://github.com/Irishbecky91/student_rations)

The deployment for the project is accredited to the code institute walkthrough project I think therefore I blog.

Design Thinking and Agile 

- Empathise Put ourselves in the user's position. Anticipate the user's wants and needs.

- Question Why would a user want to visit our blog? W
           What would make them return?

- Thinking What do I want to see when I visit a blog?
  What would make me return?

  Design thinking is accredited to the course and walkthrough I think there I blog from the code institute.
The creation of the kanban was in the github repository was shown on the I think therefore I blog walkthrough from the Code Institute.

The implementation of the user stories into the kanban and the Agile approach were shown from the course create user story template on github content of the Agile section from the code institute.

Installing Django and the supporting libraries was shown in the walkthough video I think therefore I blog. 

Creation of a new blank Django project and app was shown in the walkthough video I think therefore I blog. 

 To set our project to use Cloudinary and PostgreSQL was shown in the walkthough video I think therefore I blog.

 The deployment of the project to Heroku was shown in the walkthough video I think therefore I blog.

 The code added to the  procfile, models, settings and env files was shown in the walkthrough video I think therefore I blog.

 The creation of the templates, media and static fies was shown in the walkthrough video I think therefore I blog.

 The creation of the admin panel using the superuser in django was shown in the walkthrough video I think therefore I blog.

 The code added to the admin file was shown in the walkthrough video I think therefore I blog.

 Adding code to the admin, settings and  urls file was shown in the walkthrough video I think therefore I blog.

 The addition of summernote library was shown in the walkthrough video I think therefore I blog.

 The code added for the view files was shown in the walkthrough video I think therefore I blog.

 The setting up of the base, index and post_detail files with the code and placed into the templates folder  was shown in the walkthrough video I think therefore I blog.


The setting up of the style/css file with the code and placed in the static file was shown in the walkthrough video I think therefore I blog.

The code content for adding to the index file was shown in the walkthrough video I think therefore I blog.

The setting up of the urls file into the blog folder and adding the code was shown in the walkthrough video I think therefore I blog.

The code added to the urls file in the petstar folder was shown in the walkthrough video I think therefore I blog.

The moving of the site pagination, view likes and view post list to the done section of the kanban board for agile development was shown in the walkthrough video I think therefore I blog.

The moving of the open a post and view comments to the progress section of the kanban board was shown in the walkthrough video I think therefore I blog.

The code for the post detail view added to the view file was shown in the walkthrough video I think therefore I blog.

The code content added to the post_detail file was shown in the walkthrough video I think therefore I blog.

The code added to the urls file in the blog folder was shown in the walkthrough video I think therefore I blog.

The code added to index file was shown in the walkthrough video I think therefore I blog.

The open a post and view comments user stories were moved to the done section of the kanban board was shown in the walkthrough video I think therefore I blog.

The account registration user story moved to in progress section of the kanban board was shown in the walkthrough video I think therefore I blog.

The code added to the settings file for the installed apps was shown in the walkthrough video I think therefore I blog.

The code added to the urls file in the petstar folder was shown in the walkthrough video I think therefore I blog.

The code added to the settings file for the installed apps, site and redirect url for allauth was shown in the walkthrough video I think therefore I blog.

The code added to the base html for account logout, signup and login was shown in the walkthrough video I think therefore I blog.

To create  multiple directories in our templates folder was shown in the walkthrough video I think therefore I blog.

To add and modify the code in the login.html template was shown in the walkthrough video I think therefore I blog.

The code added to and modified to the logout and signup templates was shown in the walkthrough video I think therefore I blog.

To create the forms file and to add code to it and to the settings file was shown in the walkthrough video I think therefore I blog.

To install the django-crispy-forms was shown in the walkthrough video I think therefore I blog.

To add code to the views file was was shown in the walkthrough video I think therefore I blog.

To add code to the post detail template was shown in the walkthrough video I think therefore I blog.

To add code to the views file to show likes was shown in the walkthrough video I think therefore I blog.

To add code to the settings and base html files for the messages was shown in the walkthrough video I think therefore I blog.

On the 2nd of April I had a my first meeting with my mentor and he advised me ensure I get an update and delete function for my comments section of the blog,

I contacted tutor aupport and they sent me a youtube video from codemy and a resource link to Djasngo 

I contacted an IT and software development specialist and tutor Mike Youell for support in tutoring me in how to incorpoarate the update and delete fumtionality into the comments section.  Mike guided me through the process with the aid of a youtube video by Codemy [Codemy update & edit a blog](https://www.youtube.com/watch?v=J7xaESAddDQ). With Mikes generous support we were able to set up the update_detail,html file and input the code for that file to display the update function. This was following the Codemy video code.  Mike also explained to me in better detail what the blog urls file was doing when we inputed the code from the Codemy file.  Mike also explained to me what a slug and an int/pk were and the difference in how they are displayed in the url browser.  We then inputted the code into the views fie for the class for updating the comments.  Mike also supported me to look at the code needed for the post_detail file within the comments section. 




To deploy the site was shown in the walkthrough video I think therefore I blog. Irish Becky's readme helped me to see how to structure the written material for the readme for the deployment process. [Irish Becky's readme](https://github.com/Irishbecky91/student_rations) I also followed the process from the walkthrough video I think therefore I blog.

was shown in the walkthrough video I think therefore I blog.











### Media

The following sites and links below were used for research purposes into developing a pet blog website.

[6 Of The Best Pet Blog Sites](https://www.thepetexpress.co.uk/blog/general-interest/6-of-the-best-pet-blogs/)

[Pressplay Pets](https://pressplaypets.com/rainbow-bridge-2/)

[The Conscious Cat](https://consciouscat.net/)

[The Blog For The Pet Express](https://www.thepetexpress.co.uk/blog/)

[Blogpaws](https://blogpaws.com/)

[Oh My Dog Blog](https://ohmydogblog.com/)

[]()

### Acknowledgments

### Disclaimer

This project has solely been developed for the purposes of education, research and learning. In accordance with the copyright design and patents act 1988 the work in this project is fair dealing for research and private study and for non-commercial purposes. Any material or work from ouside sources has been acknowledged in the credits section of the readme.

[Copyright Design and Patent Act 1988](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/957583/Copyright-designs-and-patents-act-1988.pdf)

[Uk Government guidance on copyright](https://www.gov.uk/guidance/exceptions-to-copyright)


![Agile Kanban board]()







## Credits

On the 28th of January tried to do a number of git commits for what I had done for the project.  I noticed the 29th of January that these commits did not show on my github and I did do a git push also.  Student tutors advised me to ensure that all git commits are done once code has been installed and saved in the files.
The following steps were put into the git commits on the 28th of January. The steps for these installations were shown in the Code Institute Walkthrough project I think therefore I blog.












![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome sundeepbassi,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
