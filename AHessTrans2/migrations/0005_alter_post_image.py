# Generated by Django 4.1.4 on 2022-12-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AHessTrans2', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
