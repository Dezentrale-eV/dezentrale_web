# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-31 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0040_page_draft_title'),
        ('joyous', '0003_extrainfopage_extra_title'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventsindexpage',
            name='page_ptr',
        ),
        migrations.CreateModel(
            name='CalendarPage',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
                'verbose_name': 'Calendar',
            },
            bases=('joyous.calendarpage',),
        ),
        migrations.DeleteModel(
            name='EventsIndexPage',
        ),
    ]