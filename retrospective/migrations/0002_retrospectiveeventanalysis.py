# Generated by Django 2.2.11 on 2020-03-13 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("retrospective", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="RetrospectiveEventAnalysis",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("graph_data", models.TextField()),
                ("graph_image", models.FileField(upload_to="")),
                (
                    "event",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="retrospective.RetrospectiveEvent",
                    ),
                ),
            ],
        )
    ]