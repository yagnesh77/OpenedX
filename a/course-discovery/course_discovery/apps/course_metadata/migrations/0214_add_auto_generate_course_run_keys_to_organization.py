# Generated by Django 1.11.24 on 2019-11-04 20:21


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0213_removeredirectsconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='auto_generate_course_run_keys',
            field=models.BooleanField(default=True, help_text='When this flag is enabled, the key of a new course run will be auto generated.  When this flag is disabled, the key can be manually set.', verbose_name='Automatically generate course run keys'),
        ),
    ]