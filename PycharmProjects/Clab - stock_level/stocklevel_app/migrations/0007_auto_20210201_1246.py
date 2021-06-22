# Generated by Django 3.1.5 on 2021-02-01 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocklevel_app', '0006_auto_20210201_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='warehouseflows',
            old_name='amount',
            new_name='series_amount',
        ),
        migrations.AddField(
            model_name='warehouseflows',
            name='release_amount',
            field=models.FloatField(null=True, verbose_name='Wydawana ilość'),
        ),
    ]