# Generated by Django 4.2.6 on 2024-07-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("candidates", "0004_candidate_aadhar_card_candidate_cv_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="quali",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="candidate",
            name="yop",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
