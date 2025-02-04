# Generated by Django 5.0.7 on 2024-07-26 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_employee_delete_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='news/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=50),
        ),
    ]
