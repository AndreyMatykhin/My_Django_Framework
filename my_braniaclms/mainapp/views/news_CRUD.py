from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from mainapp import models as mainapp_models


class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = mainapp_models.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.add_news",)


class NewsListView(ListView):
    model = mainapp_models.News
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset().filter(deleted=False)
        if self.request.GET.get('dateFrom'):
            qs = qs.filter(created__gte=self.request.GET.get('dateFrom'))
        if self.request.GET.get('dateTo'):
            qs = qs.filter(created__lte=self.request.GET.get('dateTo'))
        return qs


class NewsDetailView(DetailView):
    model = mainapp_models.News


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = mainapp_models.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.change_news",)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = mainapp_models.News
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.delete_news",)
