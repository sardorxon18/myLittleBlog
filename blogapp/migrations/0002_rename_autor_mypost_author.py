# Generated by Django 5.1 on 2024-08-28 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mypost",
            old_name="autor",
            new_name="author",
        ),
    ]
