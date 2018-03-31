# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import generic as generic_views
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

urlpatterns = [
    url(r'^$', generic_views.TemplateView.as_view(template_name='landing_page.html'),
        name='landing_page'),
    url(r'^impressum/', generic_views.TemplateView.as_view(template_name='impressum.html'),
        name='impressum'),
    url(r'^infrastruktur/', generic_views.TemplateView.as_view(
        template_name='infrastruktur.html'), name='infrastruktur'),
    url(r'^dokumente/', generic_views.TemplateView.as_view(template_name='dokumente.html'),
        name='dokumente'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^django-admin/', include(admin.site.urls)),
    # Wagtail
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^wagtail/', include(wagtail_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
