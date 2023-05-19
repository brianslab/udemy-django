# Generated by Django 4.1 on 2023-05-19 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_created_date_alter_post_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='publish_date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 10, 43, 32, 518597, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 10, 43, 32, 518228, tzinfo=datetime.timezone.utc)),
        ),
    ]