# Generated by Django 4.1.7 on 2023-04-08 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HallEmployee",
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
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("job", models.CharField(max_length=100, verbose_name="Job")),
                (
                    "salary",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=8, verbose_name="Salary"
                    ),
                ),
                (
                    "hall",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="hall_employees",
                        to="main.hall",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="person",
            name="role",
            field=models.CharField(
                choices=[
                    ("student", "Student"),
                    ("warden", "Warden"),
                    ("hall_clerk", "Hall Clerk"),
                    ("hmc_chairman", "HMC Chairman"),
                    ("mess_manager", "Mess Manager"),
                    ("admin", "Administrator"),
                    ("admission", "Admission Unit"),
                    ("hall_clerk", "Hall Clerk"),
                ],
                default="student",
                max_length=40,
                verbose_name="Role",
            ),
        ),
        migrations.CreateModel(
            name="HallEmployeeLeave",
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
                ("date", models.DateField(verbose_name="Date")),
                (
                    "hallemployee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="leaves",
                        to="main.hallemployee",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HallClerk",
            fields=[
                (
                    "person",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="hall_clerk",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "hall",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="hall_clerk",
                        to="main.hall",
                    ),
                ),
            ],
        ),
    ]
