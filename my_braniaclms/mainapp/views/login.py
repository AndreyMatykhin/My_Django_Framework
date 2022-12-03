__all__ = ['LoginView']

from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'
