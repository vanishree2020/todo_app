# Generated by Django 5.1.1 on 2024-09-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_required',
            field=models.IntegerField(null='False'),
            preserve_default='False',
        ),
    ]
