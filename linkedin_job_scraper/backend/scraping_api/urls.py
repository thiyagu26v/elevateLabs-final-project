from django.urls import path
from .views import ScrapeJobsView, GetVisualizationView

urlpatterns = [
    path('scrape/', ScrapeJobsView.as_view(), name='scrape-jobs'),
    path('viz/', GetVisualizationView.as_view(), name='get-viz'),
]
