# Generated by Django 4.2.5 on 2023-09-15 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate_app', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraccount',
            options={'verbose_name': 'user Profile', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'user Profile', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.AddField(
            model_name='useraccount',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
