__all__ = ['NewsView']

from django.views.generic import TemplateView
from mainapp import models as mainapp_models


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_qs"] = mainapp_models.News.objects.all()[:5]
        return context
