# Generated by Django 3.0 on 2021-02-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210217_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcreate',
            name='images',
            field=models.ImageField(default='d', upload_to='images/'),
            preserve_default=False,
        ),
    ]