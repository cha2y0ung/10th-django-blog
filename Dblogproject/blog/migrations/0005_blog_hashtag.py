# Generated by Django 4.0.4 on 2022-05-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='hashtag',
            field=models.ManyToManyField(to='blog.hashtag'),
        ),
    ]