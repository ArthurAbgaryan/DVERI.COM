from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doors/',include('doors.urls',namespace='doors')),
    path('cart/',include('cart.urls', namespace='cart')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
