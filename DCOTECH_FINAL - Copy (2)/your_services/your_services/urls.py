"""your_services URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic.base import View
import service.views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',service.views.index,name='home'),
    path('post/',service.views.post_list,name='post'),
    path('post/detail/<int:pk>',service.views.posts_detail,name='post_detail'),
    path('login/',service.views.login),
    path('reg/',service.views.regis),
    path('ruff/',service.views.ruff),
    path('signup',service.views.handleSignup,name='handleSignup'),
    path('login',service.views.handleLogin,name='handleLogin'),
    path('logout',service.views.handleLogout,name='handleLogout'),
    path('new_service',service.views.new_service,name='my_post'),
    path('search',service.views.mysearch,name='search'),
    path('add_service',service.views.add_service,name='add_Service'),
    path('add_qurry/<int:pk>',service.views.add_querry,name='add_querry'),
    path('add_ans/<int:pk>',service.views.add_ans,name='add_anss'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_update.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_updated_succ.html"),name="password_reset_complete"),
    path('show_ans/<int:pk>/',service.views.show_ans,name="show_ans"),
    path('add_like/<int:pk>',service.views.add_like,name='add_like'),
    path('profile',service.views.myprofile,name="profile"),
    
   
    
    
    
    
 
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
