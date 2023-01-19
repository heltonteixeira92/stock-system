from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

admin.site.site_header = 'FranPri Embalagens'
admin.site.site_title = 'FranPri Admin'


urlpatterns = [
    path('', RedirectView.as_view(url='/admin')),
    path('admin/', admin.site.urls),
]
