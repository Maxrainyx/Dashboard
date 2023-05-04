# Dashboard

 Retro-dashboard for the fun service of the MMORPG game.

<h3>You can:</h3>
<p>sign and log in,</p>
<p>to proceed signing in you will receive confirmation email,</p>
<p>create post( + attach images and embed videos) if you're logged in,</p>
<p>edit or delete posts if you're the author of it,</p>
<p>create comments for the post, they have to be approved by its author to be availible,</p>
<p>there will be an email-notification for this action,</p>
<p>if you're the post author your comments will be immediately shown without your own approval,</p>
<p>you can see all the unapproved comments from other users to your posts on your profile page. </p>
<p>there you can filter them by the title, approve or delete them, also you can see the title of these posts and go to the full version,</p>
<p>there will be weekly mail delivery on Monday 10 A.M. with all posts for the previous week to all signed in users</p>
<hr>
<h3>Some screenshots:</h3>

> main page with all the posts

<img width="800" src="https://user-images.githubusercontent.com/115626270/236312844-ebf7844c-4549-41e1-a553-5328ecb86d40.png">

> detailed post with commentaries

<img width="800" src="https://user-images.githubusercontent.com/115626270/236312901-d29b6988-937b-486e-87cd-e39a2d83e365.png">

> profile page with an approval section

<img width="800" src="https://user-images.githubusercontent.com/115626270/236312770-7f58fd03-966a-44ad-83df-4fd97aa43585.png">
</p>

<hr>
<h3>Settings included:</h3>

> to send messages to console instead of actual email:

```
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'</p>
```

> to debug the project:

```
DEBUG = True
```

<hr>
<h3>Dashboard requares:</h3>
<ul>
  <li>celery</li>
  <li>django</li>
  <li>django-allauth</li>
  <li>django-ckeditor</li>
  <li>django-filter</li>
  <li>redis</li>
  <li>requests</>
</ul>

> You can use command below
 
```
pip3 install -r requirements.txt
```

<hr>

<h3>Problems TODO: </h3>

<ul>
    <li>edit sigh in and out pages</li>
    <li>split emails to one on creation and another on editing (approval) of the comment</li>
    <li>get rid of emails from auto approval of your comments to your own posts (?)</li>
</ul>
