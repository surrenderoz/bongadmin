# Generated by Django 3.0 on 2021-02-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210217_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcreate',
            name='images',
        ),
        migrations.AddField(
            model_name='testcreate',
            name='data',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
    ]
