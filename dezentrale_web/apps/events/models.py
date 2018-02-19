from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page


class EventsIndexPage(Page):
    intro = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    parent_page_types = ['wagtailcore.Page']

class EventPage(Page):
    start = models.DateTimeField()
    intro = models.CharField(max_length=250)
    description = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('start'),
        FieldPanel('intro'),
        FieldPanel('description'),
    ]
    parent_page_types = ['EventsIndexPage']

