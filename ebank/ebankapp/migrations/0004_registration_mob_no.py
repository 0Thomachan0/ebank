# Generated by Django 4.2.7 on 2023-11-04 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ebankapp", "0003_registration_mail_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="registration",
            name="mob_no",
            field=models.IntegerField(default="1234567890"),
            preserve_default=False,
        ),
    ]
