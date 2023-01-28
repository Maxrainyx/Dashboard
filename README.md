# Dashboard

 Dashboard for the fun service of the MMORPG game.

<h3>You can:</h3>
<p>sign and log in,</p>
<p>to proceed signing in you will receive confirmation email,</p>
<p>create post( + attach images and embed videos) if you're logged in,</p>
<p>edit or delete posts if you're the author of it,</p>
<p>create comments for the post, they have to be approved by its author to be availible,</p>
<p>there will be an email-notification for this action,</p>
<p>if you're the post author your comments will be immediately shown without your own approval,</a>
<p>you can see all the unapproved comments from other users to your posts on your profile page. </p>
<p>there you can filter them by the title, approve or delete them, also you can see the title of these posts and go to the full version,</p>
<p>there will be weekly mail delivery on Monday 10 A.M. with all posts for the previous week to all signed in users</p>
<hr>
<h3>Settings included:</h3>
  - to send messages to console instead of actual email
   <p>if DEBUG:</p>
   <p>    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'</p>
  - to debug the project
   <p>DEBUG = True</p>
<hr>
<h3>Dashboard requares:</h3>
  <p>django</p>
  <p>django-allauth</p>
  <p>django-ckeditor</p>
  <p>django-filter</p>
  <p>celery</p>
  <p>redis</p>
  <hr>
<h3>Problems TODO: </h3>
<p>move css from templates</p>
<p>edit sigh in and out pages</p>
<p>split emails to one on creation and another on editing (approval) of the comment</p>
<p>get rid of emails from auto approval of your comments to your own posts (?)</p>
<p>get rid of unused bootstrap css (?)</p>
