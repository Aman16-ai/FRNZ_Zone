# Generated by Django 3.2.13 on 2022-06-20 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frnz_Accounts', '0004_user_profile_fullname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend_request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sender_user', models.CharField(max_length=100)),
                ('receiver_user', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2022, 6, 20, 12, 43, 12, 277421))),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='user_profile',
            name='friends',
            field=models.ManyToManyField(related_name='_Frnz_Accounts_user_profile_friends_+', to='Frnz_Accounts.user_profile'),
        ),
    ]
