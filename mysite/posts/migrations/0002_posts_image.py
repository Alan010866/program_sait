# Generated by Django 4.1.5 on 2023-02-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/', verbose_name='Фото'),
        ),
    ]
