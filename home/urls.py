from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from home import views

admin.site.site_header = "Saurab's Admin"
admin.site.site_title = "Bikes Admin Portal"
admin.site.index_title = "Welcome to Saurab's Bike Researcher Portal"

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('contact', views.contact),
    path('about', views.about),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
