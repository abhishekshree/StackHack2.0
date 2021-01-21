
from django.contrib import admin
from django.urls import path
from . import views
from customers.views import register, loginPage, logoutUser, preview
from meals.views import menu, cart, updateItem, admin_dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('preview/', preview, name='preview'),
    path('menu/', menu, name='menu'),
    path('meal/', cart, name='cart'),
    path('update_item/', updateItem, name='updata_item'),
    path('admin-dashboard', admin_dashboard, name='admin_dashboard')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)