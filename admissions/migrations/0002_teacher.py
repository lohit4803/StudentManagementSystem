# Generated by Django 3.2.7 on 2021-09-14 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('exp', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
    ]