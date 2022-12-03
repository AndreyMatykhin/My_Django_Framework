__all__ = ['DocSiteView']

from django.views.generic import TemplateView


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'
