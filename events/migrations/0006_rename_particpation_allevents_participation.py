# Generated by Django 4.1.7 on 2023-03-31 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_allevents_banner_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allevents',
            old_name='particpation',
            new_name='participation',
        ),
    ]
