"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from App import views


urlpatterns = [
    path('', views.index_view, name = 'index'),
    path('signup', views.signup_view, name = 'signup'),
    path('logout', views.logout_view, name = 'logout'),
    path('login', views.login_view, name = 'login'),
    path('add_new_source', views.add_new_source, name = 'add_source'),  
    path('update_source', views.update_source, name = 'update_source'),  
    path('delete_source', views.delete_source, name = 'delete_source'),
    path('source/<int:id>', views.source_view, name = 'source_view'),  
    path('privacy', views.privacy_view, name = 'privacy_view'),  

]
