# Generated by Django 1.11.11 on 2018-05-11 14:06


import djchoices.choices
from django.db import migrations, models

from course_discovery.apps.course_metadata.choices import CourseRunStatus


def change_runs_null_state_to_unpublished(apps, schema_editor):
    CourseRun = apps.get_model('course_metadata', 'CourseRun')
    for course_run in CourseRun.objects.filter(status=''):
        course_run.status = CourseRunStatus.Unpublished
        course_run.save()


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0082_person_salutation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courserun',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('unpublished', 'Unpublished')], db_index=True, default='unpublished', max_length=255, validators=[djchoices.choices.ChoicesValidator({'published': 'Published', 'unpublished': 'Unpublished'})]),
        ),
        migrations.RunPython(change_runs_null_state_to_unpublished, migrations.RunPython.noop),
    ]
