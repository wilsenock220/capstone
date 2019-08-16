
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from django.views.generic import TemplateView

from accounts.views import AgentRegistrationView, AgentProfileCreateView, AgentLisView
from pages.views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('about/', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    path('agents/', AgentLisView.as_view(), name='agent_list'),
    
    # AUTH urls
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', AgentRegistrationView.as_view(), name='register'),
    path('register/success/', AgentProfileCreateView.as_view(), name='registration_success'),
    
    #includes to other apps URLConfigs
    path('account/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('properties/', include('properties.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)