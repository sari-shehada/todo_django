# Generated by Django 4.2.4 on 2023-09-01 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=500)),
                ('isFinished', models.BooleanField()),
                ('postedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_api.appuser')),
            ],
        ),
    ]
