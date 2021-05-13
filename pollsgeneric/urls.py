from django.urls import path
from . import views

app_name = "pollsgeneric"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index_generic'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail_generic'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results_generic'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]