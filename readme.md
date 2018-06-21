# CV-Generator [![Build Status](https://travis-ci.org/Biswajee/CV-Generator.svg?branch=master)](https://travis-ci.org/Biswajee/CV-Generator)

## About this repository
This repository is a live web app deployed on Heroku. [Click here](https:\\resumenow.herokuapp.com) to visit the web application. This web application helps users create resumes by logging into their account and filling up their details.

An API support for this application is being developed which helps distribution of user's resume data in json format that could be used by:
+ companies to review user's information .
+ artificial intelligence powered applications to evaluate user's json data.
+ online advertisement agencies to publicize individuals so that they get hired.

With a traditional resume, the above goals are either inaccurate or cannot be used in above fields.
For example, a person's name could be a skill. [(say, Ruby !)](https://en.wikipedia.org/wiki/Ruby_(given_name))

And advertisement before HRs with your skills are always a good way to upsell yourself ! :P

## Technology checkup
Time to check mark technical details. The web application uses :
+ Django
+ A lot of Python
+ HTML, CSS, JavaScript
+ And your valuable time :P

Thanks for coming here !

## Folder Structure

After you've cloned this repository, let's verify the folder structure.

        .
        │   .gitignore
        │   credentials.txt
        │   db.sqlite3
        │   manage.py
        │   Procfile
        │   readme.md
        │   requirements.txt
        │
        ├───api
        │   │   admin.py
        │   │   apps.py
        │   │   models.py
        │   │   tests.py
        │   │   urls.py
        │   │   views.py
        │   │   __init__.py
        │   │
        │   ├───migrations
        │   │       __init__.py
        │   │
        │   └───__pycache__
        │           urls.cpython-36.pyc
        │           views.cpython-36.pyc
        │           __init__.cpython-36.pyc
        │
        ├───CVGen
        │   │   settings.py
        │   │   urls.py
        │   │   wsgi.py
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │           settings.cpython-36.pyc
        │           urls.cpython-36.pyc
        │           wsgi.cpython-36.pyc
        │           __init__.cpython-36.pyc
        │
        └───webapp
        │   admin.py
        │   apps.py
        │   models.py
        │   tests.py
        │   urls.py
        │   views.py
        │   __init__.py
        │
        ├───migrations
        │   │   0001_initial.py
        │   │   0002_auto_20180617_2059.py
        │   │   0003_auto_20180618_0327.py
        │   │   0004_auto_20180618_0329.py
        │   │   0005_auto_20180618_0329.py
        │   │   0006_auto_20180618_0329.py
        │   │   0007_auto_20180618_0331.py
        │   │   0008_auto_20180618_0332.py
        │   │   0009_auto_20180618_2135.py
        │   │   0010_auto_20180618_2213.py
        │   │   0011_auto_20180618_2213.py
        │   │   0012_auto_20180618_2238.py
        │   │   0013_auto_20180619_0423.py
        │   │   0014_auto_20180619_0426.py
        │   │   0015_auto_20180619_0432.py
        │   │   0016_auto_20180619_0442.py
        │   │   0017_auto_20180619_0451.py
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │           0001_initial.cpython-36.pyc
        │           0002_auto_20180617_2059.cpython-36.pyc
        │           0003_auto_20180618_0327.cpython-36.pyc
        │           0004_auto_20180618_0329.cpython-36.pyc
        │           0005_auto_20180618_0329.cpython-36.pyc
        │           0006_auto_20180618_0329.cpython-36.pyc
        │           0007_auto_20180618_0331.cpython-36.pyc
        │           0008_auto_20180618_0332.cpython-36.pyc
        │           0009_auto_20180618_2135.cpython-36.pyc
        │           0010_auto_20180618_2213.cpython-36.pyc
        │           0011_auto_20180618_2213.cpython-36.pyc
        │           0012_auto_20180618_2238.cpython-36.pyc
        │           0013_auto_20180619_0423.cpython-36.pyc
        │           0014_auto_20180619_0426.cpython-36.pyc
        │           0015_auto_20180619_0432.cpython-36.pyc
        │           0016_auto_20180619_0442.cpython-36.pyc
        │           0017_auto_20180619_0451.cpython-36.pyc
        │           __init__.cpython-36.pyc
        │
        ├───static
        │   ├───css
        │   │   │   bootstrap.css
        │   │   │   custom_css.css
        │   │   │   main2.css
        │   │   │   slick.css
        │   │   │
        │   │   ├───font-awesome-4.7.0
        │   │   │   ├───css
        │   │   │   │       font-awesome.min.css
        │   │   │   │       font-awesome1.css
        │   │   │   │
        │   │   │   ├───fonts
        │   │   │   │       fontawesome-webfont.svg
        │   │   │   │       fontawesome-webfont.woff
        │   │   │   │       fontawesome-webfont.woff2
        │   │   │   │       FontAwesome.otf
        │   │   │   │
        │   │   │   ├───less1
        │   │   │   │       animated.less
        │   │   │   │       bordered-pulled.less
        │   │   │   │       core.less
        │   │   │   │       fixed-width.less
        │   │   │   │       font-awesome.less
        │   │   │   │       icons.less
        │   │   │   │       larger.less
        │   │   │   │       list.less
        │   │   │   │       mixins.less
        │   │   │   │       path.less
        │   │   │   │       rotated-flipped.less
        │   │   │   │       screen-reader.less
        │   │   │   │       stacked.less
        │   │   │   │       variables.less
        │   │   │   │
        │   │   │   └───scss
        │   │   │           font-awesome.scss
        │   │   │           _animated.scss
        │   │   │           _bordered-pulled.scss
        │   │   │           _core.scss
        │   │   │           _fixed-width.scss
        │   │   │           _icons.scss
        │   │   │           _larger.scss
        │   │   │           _list.scss
        │   │   │           _mixins.scss
        │   │   │           _path.scss
        │   │   │           _rotated-flipped.scss
        │   │   │           _screen-reader.scss
        │   │   │           _stacked.scss
        │   │   │           _variables.scss
        │   │   │
        │   │   └───slick-1.8.0
        │   │       │   .gitignore
        │   │       │   bower.json
        │   │       │   component.json
        │   │       │   CONTRIBUTING.markdown
        │   │       │   index.html
        │   │       │   ISSUE_TEMPLATE.md
        │   │       │   LICENSE
        │   │       │   Makefile
        │   │       │   package.json
        │   │       │   README.markdown
        │   │       │   slick.jquery.json
        │   │       │
        │   │       └───slick
        │   │           │   ajax-loader.gif
        │   │           │   config.rb
        │   │           │   slick-theme.css
        │   │           │   slick-theme.less
        │   │           │   slick-theme.scss
        │   │           │   slick.css
        │   │           │   slick.less
        │   │           │   slick.scss
        │   │           │
        │   │           └───fonts
        │   │                   slick.svg
        │   │                   slick.woff
        │   │
        │   ├───images
        │   │       00000000383.jpg
        │   │       00000000384.jpg
        │   │       00000000385.jpg
        │   │       14.png
        │   │       3306.png
        │   │       403244634.jpg
        │   │       5130.png
        │   │       56298615.jpg
        │   │       apple-phone.png
        │   │       django.png
        │   │       EpicInstaller-7.9.2-unrealengine.msi
        │   │       favicon.png
        │   │       location-vector-img.png
        │   │       mdscene.jpg
        │   │       mobile.png
        │   │       pbeach.jpg
        │   │       resumeicon.png
        │   │       sFj7Wme.png
        │   │       slide1.jpg
        │   │       Unreal Engine 4 Tutorial for Beginners - Free UE4 Training.mp4.crdownload
        │   │       Your-payment.jpg
        │   │
        │   └───js
        │           bootstrap.js
        │           jquery.min.js
        │           jquery.scrollex.min.js
        │           jquery.scrolly.min.js
        │           main.js
        │           parallax.min.js
        │           skel.min.js
        │           slick.js
        │           util.js
        │
        ├───templates
        │   └───webpages
        │           404.html
        │           fillform.html
        │           good_resume.html
        │           header.html
        │           index.html
        │           read_docs.html
        │           signin.html
        │           signup.html
        │           signupdata.html
        │
        └───__pycache__
              admin.cpython-36.pyc
              models.cpython-36.pyc
              urls.cpython-36.pyc
              views.cpython-36.pyc
              __init__.cpython-36.pyc

## Feedback

Your feedback and suggestions on any part of this application is welcome. Please head over to [Contributions](CONTRIBUTING.md) to read the guidelines for making contributions. If you wish to drop suggestions via email, feel free to write to roy.biswajeet161@gmail.com.

## Running the web application

Once you are done verifying the folder structure, run this web application locally and begin exploring. You must have Anaconda distribution installed before proceeding. If you would like to get one. Head [here](https://anaconda.org).

Once you are good to go...
Type out the following after you `cd` into the project directory :

### Setting up the environment
Note : You can rename the `myenv` identifier to any other name of your choice.
+ `conda create --name myenv`
+ `conda activate myenv`
+ `pip install requirements`

### Running the Django server

+ `python manage.py makemigrations`
+ `python manage.py migrate`
+ `python manage.py runserver`

### Knowing what's Running
Head over to http://localhost:8000 or http://127.0.0.1:8000 to find the development server serving the project's home page.

### Finishing steps
Once you are done with exploration, you may shut down the server with :
+  Ctrl+C
+ Then `conda source deactivate`

## Debugging the application
+ Chrome Dev Tools are a great fun in understanding what's taking time when rendering pages. Also, can help checking out cookies.
+ The web application has `Debug=True` set. Please read [Contributions](CONTRIBUTING.md) on how to report errors.
+ Alternatively, you can use Django's default test runner using `python manage.py test` after including the tests.

## Common troubleshoots
+ Unable to Sign in or Sign up: <br>
    Make sure you followed each and every step above carefully without errors.
    Possible reasons:
    + The database might not be created.
    + Cookies are disabled in browser.
    
