from django.urls import path
from .import views
urlpatterns = [
    path('', views.CustomerListview.as_view(), name='custom_list_view'),
    path('test/', views.render_pdf_view, name='index'),
    path('pdf/<int:pk>/', views.customer_render_pdf, name='customer_render_pdf'),
]
