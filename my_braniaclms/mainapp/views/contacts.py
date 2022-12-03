__all__ = ['ContactsView']

from django.views.generic import TemplateView


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'
