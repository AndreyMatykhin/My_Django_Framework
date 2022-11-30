# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import json


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


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


class NewsPaginatorView(NewsView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context
