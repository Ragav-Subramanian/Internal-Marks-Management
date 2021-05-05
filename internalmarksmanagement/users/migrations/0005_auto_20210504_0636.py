# Generated by Django 3.2 on 2021-05-04 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='batch',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(default='Computer Science Engineering', max_length=50),
        ),
    ]