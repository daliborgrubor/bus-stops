# Generated by Django 4.1.7 on 2023-03-04 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busstops', '0002_rename_todo_stoppoint'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StopPoint',
            new_name='BusStops',
        ),
    ]
