# Generated by Django 5.0.1 on 2024-01-22 20:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0003_board_alter_user_user_name_task"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="board_id",
            new_name="board",
        ),
    ]
