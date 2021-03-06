# Generated by Django 3.0.8 on 2020-08-14 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(default='To be added at a later date', max_length=500),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_img',
            field=models.URLField(default='https://image.flaticon.com/icons/svg/545/545837.svg'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
