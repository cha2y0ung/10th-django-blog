# Generated by Django 4.0.3 on 2022-05-29 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='introduce',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
