# Generated by Django 5.0.1 on 2024-01-22 20:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0004_rename_board_id_task_board"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="timestamp",
            new_name="time_stamp",
        ),
    ]