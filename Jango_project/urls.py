from django.contrib import admin
from django.urls import path, include
from blog import views  # добавляем импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', views.post_list, name='home'),  # главная страница
]