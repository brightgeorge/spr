# Generated by Django 4.1.7 on 2023-02-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=100)),
                ('student_name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=20)),
                ('student_description', models.TextField()),
                ('user_flage', models.IntegerField()),
            ],
        ),
    ]