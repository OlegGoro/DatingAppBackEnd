# Generated by Django 2.1.4 on 2019-01-05 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_auto_20190106_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claims',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='api/static/media/'),
        ),
    ]
