# Generated by Django 4.2.7 on 2023-11-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0003_student_accountnumber_student_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='accountnumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
