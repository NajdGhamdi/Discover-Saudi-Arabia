# Generated by Django 4.1.3 on 2022-11-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0002_site_event_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
