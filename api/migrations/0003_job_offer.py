# Generated by Django 4.0.5 on 2022-06-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_companyreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='offer',
            field=models.BooleanField(default=True),
        ),
    ]
