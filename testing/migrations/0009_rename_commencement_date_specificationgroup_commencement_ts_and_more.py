# Generated by Django 5.0.4 on 2024-05-03 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0008_alter_specificationgroup_commencement_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specificationgroup',
            old_name='commencement_date',
            new_name='commencement_ts',
        ),
        migrations.RenameField(
            model_name='specificationgroup',
            old_name='expiration_date',
            new_name='expiration_ts',
        ),
    ]
