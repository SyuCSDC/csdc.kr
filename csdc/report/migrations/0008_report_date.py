# Generated by Django 5.0.1 on 2024-02-04 08:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_alter_reportfile_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
