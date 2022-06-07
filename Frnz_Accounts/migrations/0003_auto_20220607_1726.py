# Generated by Django 3.2.13 on 2022-06-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frnz_Accounts', '0002_auto_20220605_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='fullname',
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='about',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='collage',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='interests',
            field=models.ManyToManyField(blank=True, null=True, to='Frnz_Accounts.Interset'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='want_synergy',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
