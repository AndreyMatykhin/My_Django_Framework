from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('courses/', views.CoursesListView.as_view(), name='courses'),
    path("courses/<int:pk>/", views.CoursesDetailView.as_view(), name="courses_detail", ),
    path('docsite/', views.DocSiteView.as_view(), name='doc_site'),
    path('', views.IndexView.as_view(), name='main_page'),
    path('news/', views.NewsView.as_view(), name='news'),
    path("news/<int:pk>/", views.NewsDetailView.as_view(), name="news_detail")
]
