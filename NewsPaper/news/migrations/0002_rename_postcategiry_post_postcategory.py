# Generated by Django 4.1.1 on 2022-09-08 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='postCategiry',
            new_name='postCategory',
        ),
    ]
