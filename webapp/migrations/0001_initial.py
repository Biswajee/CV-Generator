# Generated by Django 2.0.4 on 2018-06-15 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg_info',
            fields=[
                ('usr_id', models.IntegerField(default=27, primary_key=True, serialize=False, unique=True)),
                ('email', models.TextField(unique=True)),
                ('password', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]