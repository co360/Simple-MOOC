# Generated by Django 3.0.6 on 2020-05-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='slug',
            field=models.SlugField(default='teste-slug', max_length=100, unique=True, verbose_name='Identificador'),
            preserve_default=False,
        ),
    ]