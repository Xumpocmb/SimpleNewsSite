from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name="news"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.NewDetailed.as_view(), name="new-detail"),
    path('<int:pk>/update', views.NewUpdate.as_view(), name="new-update"),
    path('<int:pk>/delete', views.NewDelete.as_view(), name="new-delete"),
]