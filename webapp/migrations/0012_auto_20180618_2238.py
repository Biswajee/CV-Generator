# Generated by Django 2.0.4 on 2018-06-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20180618_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_info',
            name='usr_id',
            field=models.IntegerField(default=144, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='resume_data',
            name='cgpa',
            field=models.TextField(),
        ),
    ]