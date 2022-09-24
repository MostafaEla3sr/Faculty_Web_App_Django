# Generated by Django 4.1.1 on 2022-09-19 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_delete_doctor_delete_subject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Subject Name')),
                ('hours', models.IntegerField(default=3, verbose_name='Subject hours')),
            ],
        ),
        migrations.CreateModel(
            name='TeachingAssistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('students', models.ManyToManyField(to='pages.profile')),
            ],
        ),
    ]