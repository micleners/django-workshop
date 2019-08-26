# Generated by Django 2.2.4 on 2019-08-26 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='events.Location'),
        ),
    ]
