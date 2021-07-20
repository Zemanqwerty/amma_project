from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin_page/', include('admin_page.urls')),
    path('', views.index_page, name='index_page'),
    path('prices/', views.prices_page, name='prices_page'),
    path('massages/', views.massages_page, name='massages_page'),
    path('massages/<int:id_serv>', views.cur_massage_page, name='cur_massage_page'),
    path('massages/<int:id_serv>/<int:price>/<int:time>', views.cur_massage_page_mail, name='cur_massage_page_mail'),
    path('spa/', views.spa_page, name='spa_page'),
    path('spa/<int:id_serv>', views.cur_spa_page, name='cur_spa_page'),
    path('spa/<int:id_serv>/<int:price>/<int:time>', views.cur_spa_page_mail, name='cur_spa_page_mail'),
    path('spa_for_two/', views.spa_for_two_page, name='spa_for_two_page'),
    path('spa_for_two/<int:id_serv>', views.cur_spa_for_two_page, name='cur_spa_for_two_page'),
    path('spa_for_two/<int:id_serv>/<int:price>/<int:time>', views.cur_spa_for_two_page_mail, name='cur_spa_for_two_page_mail'),
    path('certificates/', views.certificates_page, name='certificates_page'),
    path('certificates/<int:id_certificate>/', views.cur_certificate, name='cur_certificate'),
    path('aboniments/', views.aboniment_page, name='aboniments_page'),
    path('aboniments/<int:id_aboniment>/', views.cur_aboniment, name='cur_aboniment'),
    path('certificates/certificate_create_successful/', views.certificate_s, name='certificate_s'),
    path('reviews/', views.reviews, name='reviews'),
    path('appli_online_page/', views.appli_online_page, name='appli_online_page'),
    path('workers_page/', views.workers_page, name='workers_page'),
    path('gallery/', views.gallery_page, name='gallery_page'),
    path('hamam/', views.hamam_page, name='hamam_page'),
    path('hamam/<int:id_serv>/<int:price>/<int:time>', views.cur_hamam_page_mail, name='cur_hamam_page_mail'),
    path('salt/', views.salt_page, name='salt_page'),
    path('salt/<int:id_serv>/<int:price>/<int:time>', views.cur_salt_page_mail, name='cur_salt_page_mail'),
    path('hidromassage/', views.hidromassage_page, name='hidromassage_page'),
    path('hidromassage/<int:id_serv>/<int:price>/<int:time>', views.cur_hidromassage_page_mail, name='cur_hidromassage_page_mail'),
    path('actions/', views.actions_page, name='actions_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
