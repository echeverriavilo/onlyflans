# Generated by Django 3.2.4 on 2024-06-11 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_testimonio'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='sin_azucar',
            field=models.BooleanField(default=False),
        ),
    ]
