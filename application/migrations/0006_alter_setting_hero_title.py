# Generated by Django 4.1.7 on 2023-04-12 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_alter_program_study_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='hero_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]