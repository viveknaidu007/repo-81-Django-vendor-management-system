from django.urls import path
from vendor_app import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('POST/api/vendors/', views.vendor_create),
    path('GET/api/vendors/',views.vendor_list),
    path('GET/api/vendors/<str:vendor_id>/',views.vendor_retrive),
    path('PUT/api/vendors/<str:vendor_id>',views.vendor_update),
    path('DELETE /api/vendors/<str:vendor_id>',views. vendor_destroy),
    path('POST/api/purchase_orders/', views. purchase_order_create),
    path('GET/api/purchase_orders/', views.purchase_order_list),
    path('GET/api/purchase_orders/<str:po_number>/', views.purchase_order_retrieve),
    path('PUT/api/purchase_orders/<str:po_number>', views.purchase_order_update),
    path('DELETE/api/purchase_orders/<str:po_number>', views.purchase_order_destroy),
    path('GET/api/vendors/<str:vendor_id>/performance/',views.vendor_performance),
    path('POST/api/purchase_orders/<str:po_number>/acknowledge', views.acknowledge_update),
    path('apitoken/', obtain_auth_token)
   
]

