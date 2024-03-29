# Generated by Django 5.0.2 on 2024-02-16 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('report', '__first__'),
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('', '상태를 선택하세요'), ('Active', 'Active'), ('Completed', 'Completed'), ('Pending', 'Pending')], max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.book')),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentorships_as_mentee', to='user.userprofile')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentorships_as_mentor', to='user.userprofile')),
            ],
        ),
    ]
