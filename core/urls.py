from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newsletter.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='newsletter/login.html', next_page='home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
    # Serve static and media files from development server
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # Add any production-specific URL patterns here
    pass