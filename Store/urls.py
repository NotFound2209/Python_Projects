from django.urls import path
from Store import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include


urlpatterns = [
    path('', views.home, name='Home'),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)