# Generated by Django 3.1.5 on 2021-01-27 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocklevel_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouserelease',
            name='measure',
        ),
        migrations.RemoveField(
            model_name='warehouserelease',
            name='component',
        ),
        migrations.AddField(
            model_name='warehouserelease',
            name='component',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stocklevel_app.component'),
        ),
    ]