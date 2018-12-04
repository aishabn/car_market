
from django.contrib import admin
from django.urls import path
from cars import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', views.car_list, name='car-list'),
    path('cars/detail/<int:car_id>/', views.car_detail, name='car-detail'),

    path('cars/create', views.car_create, name='car-create'),
    path('cars/update/<int:car_id>/', views.car_update, name='car-update'),
    path('cars/delete/<int:car_id>/', views.car_delete, name='car-delete'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)