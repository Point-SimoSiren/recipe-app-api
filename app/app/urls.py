from django.contrib import admin
from django.urls import path, include
import user.urls


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/recipe/', include('recipe.urls')),
]
