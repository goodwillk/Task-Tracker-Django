# Generated by Django 4.1.7 on 2023-02-20 06:18

from django.db import migrations, models
import task.models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0003_alter_taskdetail_assigned_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskdetail",
            name="assigned_time",
            field=models.DateTimeField(default=task.models.TaskDetail.assigned),
        ),
    ]
