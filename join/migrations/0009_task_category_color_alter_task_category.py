# Generated by Django 5.0.6 on 2024-06-01 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0008_alter_task_board_alter_task_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category_color',
            field=models.CharField(default='#000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(default='main', max_length=20),
        ),
    ]
