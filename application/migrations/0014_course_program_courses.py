# Generated by Django 4.1.7 on 2023-04-14 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_alter_lecture_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.AddField(
            model_name='program',
            name='courses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='application.course'),
        ),
    ]