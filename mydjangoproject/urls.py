"""
URL configuration for mydjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from myapp1 import views
from myapp1.views import index_page, film_page, order_page, text, about_page, login_page

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name = 'index'),
    path('login_index.html', login_page),
    path('film.html', film_page),
    path('order.html', order_page),

    path('text.html', text),
    path('about', about_page),


    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('login/', auth_views.LoginView.as_view(), name = 'login_index'),

    path('search.html', index_page),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)