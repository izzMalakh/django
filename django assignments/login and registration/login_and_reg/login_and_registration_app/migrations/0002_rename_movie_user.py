# Generated by Django 4.1.1 on 2022-10-02 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_registration_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie',
            new_name='User',
        ),
    ]
