# Generated by Django 2.1.7 on 2019-02-25 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20190225_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='events.Event'),
        ),
    ]
