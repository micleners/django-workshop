# Generated by Django 2.2.4 on 2019-08-26 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('company', models.CharField(blank=True, max_length=256)),
                ('address', models.CharField(blank=True, max_length=256)),
                ('description', models.TextField(blank=True)),
                ('contact_primary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact_primary', to=settings.AUTH_USER_MODEL)),
                ('contact_secondary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact_secondary', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
