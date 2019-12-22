from django.urls import path
from .views import ShowListView, ShowDetailView

urlpatterns = [
    path('', ShowListView.as_view()),
    path('<pk>', ShowDetailView.as_view())
]
