# Generated by Django 4.1.5 on 2023-01-24 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.ManyToManyField(default=False, to='board.post'),
        ),
    ]
