# Generated by Django 4.2.4 on 2023-08-14 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lanternDie', '0006_profiles_profpic_alter_kill_image1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kill',
            old_name='image1',
            new_name='image',
        ),
    ]
