# Generated by Django 2.1.3 on 2018-11-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='no',
            field=models.IntegerField(verbose_name='编号'),
        ),
    ]
