from datetime import datetime, timedelta

from django.core.mail import send_mail
from dashboard.settings import DEFAULT_FROM_EMAIL
from .models import Post, User
from celery import shared_task


@shared_task
def weekly_mail():
    new_posts = Post.objects.filter(created__gt=(datetime.today() - timedelta(days=7)))

    post_list = ''
    for post in new_posts:
        post_list += f'"{post.title}"\n Подробнее: https://127.0.0.1:8000/news/{post.id} \n'
    user_emails = [User.objects.all().values('email')['email']]
    email_subject = f"Новое за неделю!"
    email_message = post_list
    send_mail(subject=email_subject,
              message=email_message,
              from_email=DEFAULT_FROM_EMAIL,
              recipient_list=user_emails,
              )
