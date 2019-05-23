# Generated by Django 2.2 on 2019-05-23 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInstance',
            fields=[
                ('professor_name', models.CharField(help_text='Enter professor name:', max_length=40)),
                ('course_location', models.CharField(help_text='Enter course location:', max_length=20)),
                ('frequency_of_course', models.CharField(choices=[('MON', 'Monday'), ('TUES', 'Tuesday'), ('WED', 'Wednesday'), ('THURS', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], default=None, help_text='Course Frequency:', max_length=7, primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['professor_name', 'course_location', 'frequency_of_course', 'start_time', 'end_time', 'start_date', 'end_date'],
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_CRN', models.PositiveIntegerField(default=0, help_text='Enter your course CRN:', max_length=6)),
                ('course_name', models.CharField(help_text='Enter course name:', max_length=30, primary_key=True, serialize=False)),
                ('course_credits', models.PositiveIntegerField(default=0, help_text='Enter course credits:', max_length=1)),
                ('instance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.CourseInstance')),
            ],
            options={
                'ordering': ['course_CRN', 'course_name', 'course_credits'],
            },
        ),
    ]
