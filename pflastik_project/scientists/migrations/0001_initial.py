# Generated by Django 5.0.7 on 2024-07-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Expert",
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
                ("name", models.CharField(max_length=255)),
                ("field_of_expertise", models.CharField(max_length=255)),
                ("bio", models.TextField()),
                ("contact_info", models.EmailField(max_length=254)),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="expert_photos/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Publication",
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
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("abstract", models.TextField()),
                ("content", models.TextField()),
                ("published_date", models.DateField()),
                ("category", models.CharField(max_length=255)),
                ("file", models.FileField(upload_to="publications/")),
                ("external_link", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tutorial",
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
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("category", models.CharField(max_length=255)),
            ],
        ),
    ]
