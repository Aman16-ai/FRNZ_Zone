# Generated by Django 3.2.13 on 2022-06-20 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frnz_Accounts', '0007_alter_friend_request_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend_request',
            name='timestamp',
        ),
    ]