# Generated by Django 5.0.1 on 2024-02-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorship',
            name='status',
            field=models.CharField(choices=[('', '상태를 선택하세요'), ('Active', '활동'), ('Completed', '완료'), ('Pending', '보류')], max_length=20),
        ),
    ]
