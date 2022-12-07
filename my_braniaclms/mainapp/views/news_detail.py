__all__ = ['NewsDetailView']

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from mainapp import models as mainapp_models


class NewsDetailView(TemplateView):
    template_name = 'mainapp/news_detail.html'

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(mainapp_models.News, pk=pk)
        return context
