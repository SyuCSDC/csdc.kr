# Generated by Django 5.0.1 on 2024-02-03 10:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Completed', 'Completed'), ('Pending', 'Pending')], max_length=20)),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentorships_as_mentee', to=settings.AUTH_USER_MODEL)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentorships_as_mentor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
