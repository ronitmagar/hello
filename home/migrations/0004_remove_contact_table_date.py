# Generated by Django 3.1.7 on 2022-05-07 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220507_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_table',
            name='date',
        ),
    ]
