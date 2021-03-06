# Generated by Django 2.1.4 on 2019-01-03 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20190103_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatsession',
            old_name='user1',
            new_name='users',
        ),
        migrations.RemoveField(
            model_name='chatsession',
            name='user2',
        ),
        migrations.AlterField(
            model_name='messages',
            name='chatsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='music.ChatSession'),
        ),
    ]
