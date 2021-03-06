# Generated by Django 3.0 on 2021-02-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('bday', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('bio', models.TextField(max_length=100)),
                ('profileimg', models.ImageField(upload_to='')),
                ('awards', models.CharField(max_length=30)),
                ('websiteurl', models.URLField(max_length=30)),
                ('genre', models.TextField()),
                ('profession', models.TextField()),
                ('tags', models.TextField()),
                ('label', models.TextField()),
            ],
        ),
    ]
