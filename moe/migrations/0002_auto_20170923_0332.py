# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-23 03:32
from __future__ import unicode_literals

from django.db import migrations


RMS_PHOTOS = [
    "https://stallman.org/photos/rms-working/mid/mid_p1000844.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_0554.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_1755.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_3235.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_3658.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_4188.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_working-with-the-devil.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_p1000541.jpg",
]


def forwards(apps, schema_editor):
    Moe = apps.get_model('moe', 'Moe')
    for url in RMS_PHOTOS:
        moe = Moe(url=url)
        moe.save()


class Migration(migrations.Migration):

    dependencies = [
        ('moe', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, reverse_code=migrations.RunPython.noop),
    ]
