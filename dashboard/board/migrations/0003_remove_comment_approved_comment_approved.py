# Generated by Django 4.1.5 on 2023-01-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_remove_comment_approved_comment_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
