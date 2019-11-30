# Generated by Django 2.1.4 on 2019-11-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_auto_20190106_0246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatsession',
            name='users',
        ),
        migrations.AddField(
            model_name='chatsession',
            name='user1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='chatsession',
            name='user2',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
