# Generated by Django 3.1.7 on 2022-05-07 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.TextField(),
        ),
    ]
