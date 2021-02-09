# Generated by Django 3.0.11 on 2021-02-09 16:06

import codershq.users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='github_profile',
            field=models.CharField(blank=True, max_length=255, validators=[codershq.users.validators.validate_github_profile], verbose_name="User's GitHub profile"),
        ),
    ]