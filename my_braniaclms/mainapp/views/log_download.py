from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import FileResponse
from django.views.generic import View


class LogDownloadView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, *args, **kwargs):
        return FileResponse(open(settings.LOG_FILE, "rb"))
