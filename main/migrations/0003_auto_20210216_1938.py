# Generated by Django 3.0 on 2021-02-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210216_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createartist',
            name='genre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='createartist',
            name='label',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='createartist',
            name='profession',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='createartist',
            name='tags',
            field=models.CharField(max_length=100),
        ),
    ]
