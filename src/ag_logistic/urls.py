from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'baslyk.views.home', name='home'),
    url(r'^contact/', 'baslyk.views.contact', name='contact'),
    url(r'^CostCalculate/', 'baslyk.views.CostCalculate', name='CostCalculate'),
    url(r'^thanks/', 'baslyk.views.thanks', name='thanks'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)