# Generated by Django 4.1.7 on 2023-03-10 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busstops', '0006_rename_lat_busstops_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busstops',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='busstops',
            name='longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='busstops',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
