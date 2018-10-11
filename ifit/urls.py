"""ifit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api-token-auth/',obtain_jwt_token),
    path('api-token-refresh/',refresh_jwt_token),
    path('api-token-verify/',verify_jwt_token),
    path('', include('ifit.web.urls', namespace='site')),

    path('core/',include('ifit.core.urls',namespace='core')),
    path('api/v1/',include('ifit.api.urls',namespace='api')),
    path('rest-auth/',include('rest_auth.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)