# Generated by Django 4.1.2 on 2022-11-03 17:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql_start', '0006_alter_first_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
