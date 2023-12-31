# Generated by Django 4.2.2 on 2023-07-15 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lanternDie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follows', models.ManyToManyField(blank=True, related_name='followed_by', to='lanternDie.profiles')),
                ('user', models.OneToOneField(default='01', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='lanternDie',
        ),
    ]
