from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bjstatistics/', include('bjstatistics.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('home.urls'))
]
