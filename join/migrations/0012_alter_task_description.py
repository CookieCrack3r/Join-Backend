# Generated by Django 5.0.6 on 2024-06-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0011_alter_task_subtasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]