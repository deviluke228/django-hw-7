from django.urls import path

from bboard.views import index, by_rubric, BbCreateView, select_columns, exclude_values

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('select_columns/', select_columns, name='select_columns'),
    path('exclude_values/', exclude_values, name='exclude_values'),
    path('', index, name='index'),
]