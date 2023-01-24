# Dashboard

 Dashboard for the fun service of the MMORPG game.

<h3>You can:</h3>
<p>sign and log in,</p>
<p>create post( + attach images and embed videos) if you're logged in,</p>
<p>edit or delete posts if you're the author of it,</p>
<p>create comments for the post, they have to be approved by its author to be availible,</p>
<p>there will be an email-notification for this action,</p>
<p>if you're the post author your comments will be immediately shown without your approval,</a>
<p>you can see all the unapproved comments on your profile page,</p>
<p>there you can filter them by the title, approve or delete them,</p>
<p>there will be weekly mail delivery on Monday 10 A.M. with all post for the previous week to all signed in users</p>
<hr>
Settings are enabled:
  - to send messages to console instead of actual email
   <p>if DEBUG:</p>
   <p>    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'</p>
  - to debug the project
   <p>DEBUG = True</p>
<hr>
<p>Dashboard requares:</p>
  <p>django</p>
  <p>django-allauth</p>
  <p>django-ckeditor</p>
  <p>django-filter</p>
  <p>celery</p>
  <p>redis</p>
