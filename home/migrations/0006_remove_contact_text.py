# Generated by Django 3.1.7 on 2022-05-07 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20220507_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='text',
        ),
    ]