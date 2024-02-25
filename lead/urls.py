from django.urls import path

from . import views

urlpatterns = [
    path('', views.leads_list, name='leads_list'),
    path('add-lead/', views.add_lead, name='add_lead'),
    path('<int:pk>/', views.leads_detail, name='leads_details'),
    path('<int:pk>/delete', views.leads_delete, name='lead_delete'),
    path('<int:pk>/edit', views.leads_edit, name='leads_edit')
]