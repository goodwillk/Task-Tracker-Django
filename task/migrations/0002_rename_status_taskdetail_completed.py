# Generated by Django 4.1.7 on 2023-02-20 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="taskdetail",
            old_name="status",
            new_name="completed",
        ),
    ]