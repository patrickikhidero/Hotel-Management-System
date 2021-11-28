from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.urls import path

# from .views import index, about


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage),
    url(r'^about/$', views.about),
    url(r'^cart/$', views.cart),
    url(r'^checkout/$', views.checkout),
    url(r'^contact/$', views.contact),
    url(r'^page_404/$', views.page_404),
    url(r'^payment_complete/$', views.payment_complete),
    url(r'^payment_received/$', views.payment_received),
    url(r'^room_details/$', views.room_details),
    url(r'^room_grid/$', views.room_grid),
    url(r'^user_dashboard_booking/$', views.user_dashboard_booking),
    url(r'^user_dashboard_profile/$', views.user_dashboard_profile),
    url(r'^user_dashboard_reviews/$', views.user_dashboard_reviews),
    url(r'^user_dashboard_wishlist/$', views.user_dashboard_wishlist),
    url(r'^user_dashboard/$', views.user_dashboard),
    url(r'^user_profile/$', views.user_profile),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
