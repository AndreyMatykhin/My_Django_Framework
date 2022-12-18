from django.conf import settings
from collections import deque
from django.views.generic import TemplateView


class LogView(TemplateView):
    template_name = "mainapp/log_view.html"

    def get_context_data(self, **kwargs):
        context = super(LogView, self).get_context_data(**kwargs)
        with open(settings.LOG_FILE, "r") as log_file:
            context["log"] = "".join(deque(log_file, 1000))
        return context
