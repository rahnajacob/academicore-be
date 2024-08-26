# Generated by Django 5.1 on 2024-08-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0003_remove_teacherprofile_teach_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherprofile',
            name='is_teacher',
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='teach_dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
