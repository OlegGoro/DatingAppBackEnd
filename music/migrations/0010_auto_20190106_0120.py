# Generated by Django 2.1.4 on 2019-01-05 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_claims_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claims',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]
