# Generated by Django 5.0.2 on 2024-04-05 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lesson",
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
                ("name", models.CharField(max_length=100)),
                ("link", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("author", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                ("time_start", models.DateTimeField(default=0)),
                ("max_quantity_students", models.IntegerField()),
                ("min_quantity_students", models.IntegerField(default=5)),
                ("quantity_students", models.IntegerField(blank=True, null=True)),
                (
                    "lesson",
                    models.ManyToManyField(
                        blank=True, null=True, related_name="lesson", to="app.lesson"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="lesson",
            name="product",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="product", to="app.product"
            ),
        ),
        migrations.CreateModel(
            name="Groups",
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
                ("name_group", models.CharField(max_length=50)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
                (
                    "students",
                    models.ManyToManyField(blank=True, null=True, to="app.student"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AccessProduct",
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
                (
                    "access",
                    models.CharField(choices=[("N", "no"), ("Y", "yes")], max_length=1),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.student",
                    ),
                ),
            ],
        ),
    ]
