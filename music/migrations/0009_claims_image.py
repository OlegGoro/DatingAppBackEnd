# Generated by Django 2.1.4 on 2019-01-05 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20190105_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='claims',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='claims/images/'),
        ),
    ]
