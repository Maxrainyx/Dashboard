# Dashboard

 Dashboard for the fun service of the MMORPG game.

<h3>You can:</h3>
<a>sign and log in,</a>
<a>create post( + attach images and embed videos) if you're logged in,</a>
<a>edit or delete posts if you're the author of it,</a>
<a>create comments for the post, they have to be approved by its author to be availible,</a>
<a>there will be an email-notification for this action,</a>
<a>if you're the post author your comments will be immediately shown without your approval,</a>
<a>you can see all the unapproved comments on your profile page,</a>
<a>there you can filter them by the title, approve or delete them,</a>
<a>there will be weekly mail delivery on Monday 10 A.M. with mails for the previous week to all sighned in users,</a>
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
