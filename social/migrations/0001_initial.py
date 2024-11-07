# Generated by Django 5.1.3 on 2024-11-07 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('url', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_social', models.CharField(max_length=300, unique=True)),
                ('title', models.CharField(default=None, max_length=500)),
                ('url', models.CharField(default=None, max_length=1000)),
                ('thumb', models.CharField(default=None, max_length=1000)),
                ('description', models.CharField(default=None, max_length=5000)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='social.channel')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default=None, max_length=1000)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='social.video')),
            ],
        ),
    ]
