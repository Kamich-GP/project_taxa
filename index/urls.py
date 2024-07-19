from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('product/<int:pk>', views.get_exact_pr),
    path('category/<int:pk>', views.get_exact_category)
]
