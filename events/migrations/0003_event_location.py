# Generated by Django 2.1.7 on 2019-02-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
