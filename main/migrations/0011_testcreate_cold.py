# Generated by Django 3.0 on 2021-02-17 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_testcreate_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcreate',
            name='cold',
            field=models.CharField(default='d', max_length=50),
            preserve_default=False,
        ),
    ]
