"""
URL configuration for backend project.

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
from django.urls import path, include
from rest_framework import routers
from lanternDie import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
#router.register(r'lanternDie', views.ldView, 'lanternDie') #this line might need to be customized more

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path("", include("lanternDie.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
You can now perform CRUD operations on the Todo model. The router class allows you to make the following queries:

/todos/ - returns a list of all the Todo items. CREATE and READ operations can be performed here.
/todos/id - returns a single Todo item using the id primary key. UPDATE and DELETE operations can be performed here.
'''
