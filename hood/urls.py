from hood import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf import settings


urlpatterns=[
    url(r'^$', views.register, name='register'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^home/$',views.home, name='home'),
  

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)