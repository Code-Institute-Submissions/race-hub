# Generated by Django 3.1.1 on 2020-09-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_event_instance'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventinstance',
            name='race_limit',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
    ]
