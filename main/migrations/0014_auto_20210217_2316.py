# Generated by Django 3.0 on 2021-02-17 17:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_createartist_emailid'),
    ]

    operations = [
        migrations.AddField(
            model_name='createartist',
            name='createdon',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='createartist',
            name='status',
            field=models.BooleanField(default=True, verbose_name=True),
            preserve_default=False,
        ),
    ]
