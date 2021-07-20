from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login_admin_page, name='login_admin_page'),
    path('admin_control_page/', views.admin_control_page, name='admin_control_page'),
    path('admin_reviews_page/', views.admin_reviews_page, name='admin_reviews_page'),
    path('admin_reviews_page/update/<int:id_review>', views.admin_reviews_update, name='admin_reviews_update'),
    path('admin_reviews_page/delete/<int:id_review>', views.admin_reviews_delete, name='admin_reviews_delete'),
    path('admin_payment_page/', views.admin_payment_page, name='admin_payment_page'),
    path('admin_payment_page/update/<int:id_payed>', views.admin_payment_update, name='admin_payment_update'),
    path('admin_certificates_page/', views.admin_certificates_page, name='admin_certificates_page'),
    path('admin_certificates_page/<int:id_certificate>',
         views.admin_certificate_status_update,
         name='admin_certificate_status_update'),
    path('admin_aboniment_page/', views.admin_aboniment_page, name='admin_aboniment_page'),
    path('workers/', views.workers, name='workers'),
    path('workers/workers_delete/<int:id_worker>', views.workers_delete, name='workers_delete'),
    path('actions/', views.actions, name='actions'),
    path('actions/actions_delete/<int:id_action>', views.actions_delete, name='actions_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
