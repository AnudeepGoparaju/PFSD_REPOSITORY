# Generated by Django 4.1.7 on 2023-04-02 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdp', '0003_feed_transfer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='transfer',
        ),
        migrations.AlterField(
            model_name='feed',
            name='feedb',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
