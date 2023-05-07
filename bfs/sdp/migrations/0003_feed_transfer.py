# Generated by Django 4.1.7 on 2023-04-02 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdp', '0002_rename_user_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedb', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]