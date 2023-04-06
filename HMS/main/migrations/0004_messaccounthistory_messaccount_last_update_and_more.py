# Generated by Django 4.1.7 on 2023-04-06 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_messaccount_alter_boarderroom_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="MessAccountHistory",
            fields=[
                (
                    "mess_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="mess_account_history",
                        serialize=False,
                        to="main.messaccount",
                    ),
                ),
                ("last_update", models.DateField(verbose_name="Last Updated Date")),
                (
                    "due",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=8,
                        verbose_name="Mess Due",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="messaccount",
            name="last_update",
            field=models.DateField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Last Update Date",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="messaccount",
            name="paid",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=8, verbose_name="Paid"
            ),
        ),
        migrations.CreateModel(
            name="MessManager",
            fields=[
                (
                    "person",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="mess_manager",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "hall",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="mess_maanger",
                        to="main.hall",
                    ),
                ),
            ],
        ),
    ]