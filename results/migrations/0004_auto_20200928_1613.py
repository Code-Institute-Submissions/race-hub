# Generated by Django 3.1.1 on 2020-09-28 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_auto_20200926_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F'), ('N', 'Prefer not to say')], max_length=2, null=True),
        ),
    ]
