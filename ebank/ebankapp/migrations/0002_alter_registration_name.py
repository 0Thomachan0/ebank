# Generated by Django 4.2.7 on 2023-11-03 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ebankapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registration",
            name="name",
            field=models.CharField(max_length=30),
        ),
    ]
