# Generated by Django 2.2.5 on 2022-01-23 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('expected_token', models.TextField()),
            ],
        ),
    ]