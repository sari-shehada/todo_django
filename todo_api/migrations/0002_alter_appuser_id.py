# Generated by Django 4.2.4 on 2023-09-01 20:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='id',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
    ]