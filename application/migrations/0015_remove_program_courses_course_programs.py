# Generated by Django 4.1.7 on 2023-04-14 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0014_course_program_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='courses',
        ),
        migrations.AddField(
            model_name='course',
            name='programs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='application.program'),
        ),
    ]