__all__ = ['NewsPaginatorView']

from .news import NewsView


class NewsPaginatorView(NewsView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context
