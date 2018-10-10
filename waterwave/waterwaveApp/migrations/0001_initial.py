# Generated by Django 2.0.6 on 2018-10-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Waterwave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songName', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('duration', models.TimeField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]