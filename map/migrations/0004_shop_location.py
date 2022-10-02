# Generated by Django 2.2.28 on 2022-08-19 13:13

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_remove_shop_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0), geography=True, srid=4326),
        ),
    ]
