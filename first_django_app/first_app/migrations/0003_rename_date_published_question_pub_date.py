# Generated by Django 4.0.5 on 2022-06-21 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_alter_question_date_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Date_published',
            new_name='pub_date',
        ),
    ]
