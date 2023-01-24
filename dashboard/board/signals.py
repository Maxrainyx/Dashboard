from django.dispatch import receiver
from .models import Post, Comment
from django.db.models.signals import post_save
from django.core.mail import send_mail
from celery.schedules import crontab
from dashboard.settings import DEFAULT_FROM_EMAIL


@receiver(post_save, sender=Comment)
def notify_on_comment(sender, instance, **kwargs):
    """ Notification for a new comment to its owner Post """
    #  find a new comment
    new_comment = Comment.objects.all().order_by('-created').first()

    # find new comments author and then his email
    post_author_email = Post.objects.get(id=new_comment.post.id).author.email

    if new_comment:

        email_subject = f"There's a new comment to your post!"
        email_message = f'"{new_comment.post.title}"\n Подробнее: http://127.0.0.1:8000/news/{new_comment.post.id}'

        send_mail(subject=email_subject,
                  message=email_message,
                  from_email=DEFAULT_FROM_EMAIL,
                  recipient_list=[post_author_email],
                  )


app.conf.beat_schedule = {
    'weekly_mail': {
        'task': 'board.tasks.weekly_mail',
        'schedule': crontab(hour=10, minute=0, day_of_week='monday'),
    },
}