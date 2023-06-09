# Generated by Django 4.1.9 on 2023-05-18 08:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("giving", "0002_projectpledge_pledgee"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectpledge",
            name="house_choices",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Gryffindor", "Gryffindor"),
                    ("Hufflepuff", "Hufflepuff"),
                    ("Ravenclaw", "Ravenclaw"),
                    ("Slytherin", "Slytherin"),
                ],
                help_text="School house you want to support",
                max_length=50,
            ),
        ),
    ]
