# Generated by Django 2.1.3 on 2018-12-12 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0003_auto_20181121_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='unlabel_data',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='编号')),
                ('svm', models.BooleanField(verbose_name='SVM')),
                ('lr', models.BooleanField(verbose_name='LR')),
                ('dt', models.BooleanField(verbose_name='DT')),
                ('lgbm', models.BooleanField(verbose_name='LGBM')),
                ('content', models.TextField(verbose_name='正文')),
            ],
            options={
                'verbose_name_plural': '无标签数据',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='text',
            options={'ordering': ['-id'], 'verbose_name_plural': '有标签数据'},
        ),
    ]