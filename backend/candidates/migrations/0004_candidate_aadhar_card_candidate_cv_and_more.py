# Generated by Django 4.2.6 on 2024-07-04 06:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("candidates", "0003_alter_candidate_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="aadhar_card",
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name="candidate",
            name="cv",
            field=models.FileField(blank=True, null=True, upload_to="cvs/pdf/"),
        ),
        migrations.AddField(
            model_name="candidate",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="candidate",
            name="skillset",
            field=models.TextField(blank=True),
        ),
    ]
