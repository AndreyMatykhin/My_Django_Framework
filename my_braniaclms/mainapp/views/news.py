__all__ = ['NewsView']

from django.views.generic import TemplateView
import json


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        json_data = open('static/news_list.json', 'r')
        data = json.load(json_data)
        context['news_list'] = data
        json_data.close()
        context['range'] = range(1, len(data) + 1)
        return context
