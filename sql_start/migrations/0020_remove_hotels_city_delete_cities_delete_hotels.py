# Generated by Django 4.1.2 on 2022-12-14 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sql_start', '0019_cities_hotels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='city',
        ),
        migrations.DeleteModel(
            name='Cities',
        ),
        migrations.DeleteModel(
            name='Hotels',
        ),
    ]
