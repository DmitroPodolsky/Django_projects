# Generated by Django 4.1.2 on 2022-11-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql_start', '0010_alter_first_second'),
    ]

    operations = [
        migrations.CreateModel(
            name='Third',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(default='Джеки', max_length=100)),
                ('actor_famale', models.CharField(default='Чан', max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Man'), ('W', 'Women')], default='M', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='first',
            name='third',
            field=models.ManyToManyField(to='sql_start.third'),
        ),
    ]
