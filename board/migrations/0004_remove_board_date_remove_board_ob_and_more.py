# Generated by Django 5.0.7 on 2024-07-25 09:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0003_alter_board_ob_alter_board_region"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="board",
            name="date",
        ),
        migrations.RemoveField(
            model_name="board",
            name="ob",
        ),
        migrations.RemoveField(
            model_name="board",
            name="region",
        ),
        migrations.RemoveField(
            model_name="board",
            name="textbox",
        ),
        migrations.AddField(
            model_name="board",
            name="address",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="board",
            name="gu",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="board",
            name="reservation",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("body", models.TextField(max_length=1000)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("star", models.IntegerField()),
                (
                    "board",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="board.board",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]