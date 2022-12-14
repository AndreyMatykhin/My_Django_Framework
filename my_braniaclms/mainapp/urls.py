from django.urls import path
from django.views.decorators.cache import cache_page
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', views.IndexView.as_view(), name='main_page'),

    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('courses/', cache_page(60 * 5)(views.CoursesListView.as_view()), name='courses'),
    path("courses/<int:pk>/", views.CoursesDetailView.as_view(), name="courses_detail"),
    path("course_feedback/", views.CourseFeedbackFormProcessView.as_view(), name="course_feedback"),
    path('docsite/', views.DocSiteView.as_view(), name='doc_site'),
    path('news/', views.NewsListView.as_view(), name='news'),
    path("news/create/", views.NewsCreateView.as_view(), name="news_create"),
    path("news/<int:pk>/detail", views.NewsDetailView.as_view(), name="news_detail"),
    path("news/<int:pk>/update", views.NewsUpdateView.as_view(), name="news_update", ),
    path("news/<int:pk>/delete", views.NewsDeleteView.as_view(), name="news_delete", ),
    path("log_view/", views.LogView.as_view(), name="log_view"),
    path("log_download/", views.LogDownloadView.as_view(), name="log_download"),
]
