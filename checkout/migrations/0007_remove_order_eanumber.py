# Generated by Django 3.1.1 on 2020-10-01 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_eanumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='eanumber',
        ),
    ]
