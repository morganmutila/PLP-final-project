# Generated by Django 4.1.7 on 2023-04-12 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_alter_studycategory_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(upload_to='faces')),
            ],
        ),
    ]
