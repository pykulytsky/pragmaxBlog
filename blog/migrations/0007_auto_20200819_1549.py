# Generated by Django 3.1 on 2020-08-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='assets/photos/users/', verbose_name='Profile photo'),
        ),
    ]