# Generated by Django 4.2.7 on 2023-11-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0002_rename_sudent_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='accountnumber',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='amount',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]