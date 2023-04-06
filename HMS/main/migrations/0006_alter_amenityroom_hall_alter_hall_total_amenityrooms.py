# Generated by Django 4.1.7 on 2023-04-06 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_hall_total_amenityrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenityroom',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenityRooms', to='main.hall'),
        ),
        migrations.AlterField(
            model_name='hall',
            name='total_amenityrooms',
            field=models.IntegerField(default=0, verbose_name='Total Amenity Rooms'),
        ),
    ]