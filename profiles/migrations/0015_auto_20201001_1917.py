# Generated by Django 3.1.1 on 2020-10-01 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20201001_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonracehubfriends',
            name='parentprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.athleteprofile'),
        ),
    ]
