# Generated by Django 3.1.1 on 2020-10-03 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_auto_20201003_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='dateofbirth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
