# Generated by Django 4.0.6 on 2022-11-18 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('G_ARModule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Con_Student_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50, null=True)),
                ('Last_Name', models.CharField(max_length=50, null=True)),
                ('Email', models.EmailField(max_length=80, null=True)),
                ('Message', models.TextField(max_length=100, null=True)),
            ],
        ),
    ]
