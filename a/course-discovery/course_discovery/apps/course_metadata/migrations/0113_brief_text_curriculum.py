# Generated by Django 1.11.15 on 2018-09-05 12:30


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0112_degree_banner_border_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='marketing_text_brief',
            field=models.TextField(blank=True, help_text='A high-level overview of the degree\'s courseware. The "brief"\n            text is the first 300 characters of "marketing_text" and must be\n            valid HTML.', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='marketing_text',
            field=models.TextField(help_text="A high-level overview of the degree's courseware.", null=True),
        ),
        migrations.AlterField(
            model_name='degree',
            name='banner_border_color',
            field=models.CharField(blank=True, help_text='The 6 character hex value of the color to make the banner borders\n            (e.g. "#ff0000" which equals red) No need to provide the `#`', max_length=6),
        ),
    ]