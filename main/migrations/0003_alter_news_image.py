# Generated by Django 4.1.3 on 2022-11-16 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
