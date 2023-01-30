from datetime import datetime, timedelta

from django.core.mail import send_mail
from dashboard.settings import DEFAULT_FROM_EMAIL
from .models import Post, User
from celery import shared_task


@shared_task
def weekly_mail():
    """ Task to define what and where to send in e-mail """
    # new posts for the last 7 days
    new_posts = Post.objects.filter(created__gt=(datetime.today() - timedelta(days=7)))

    post_list = ''  # it's not an actual list btw :D
    for post in new_posts:
        post_list += f'"{post.title}"\n Read full at: https://127.0.0.1:8000/news/{post.id} \n'  # title+link is enough?
    user_emails = [User.objects.all().values('email')['email']]
    email_subject = f"Here is new posts for the last week for you!"
    email_message = post_list
    send_mail(subject=email_subject,
              message=email_message,
              from_email=DEFAULT_FROM_EMAIL,  # imported from .settings even if it shows "unresolved"
              recipient_list=user_emails,
              )
