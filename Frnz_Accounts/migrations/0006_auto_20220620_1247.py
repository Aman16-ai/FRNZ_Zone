# Generated by Django 3.2.13 on 2022-06-20 12:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Frnz_Accounts', '0005_auto_20220620_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend_request',
            name='receiver_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='Frnz_Accounts.user_profile'),
        ),
        migrations.AlterField(
            model_name='friend_request',
            name='sender_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='Frnz_Accounts.user_profile'),
        ),
        migrations.AlterField(
            model_name='friend_request',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 12, 47, 44, 866158)),
        ),
    ]
