from django.contrib import admin
from django.urls import path, include

# Aqui é a ligação entre a api e a livraria
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]

