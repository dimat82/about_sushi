"""About_sushi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from menu.views import IndexView
from django.conf.urls.static import static
from django.conf import settings
from contacts.views import Feedback,Contacts,Registration
from article.views import NewsList,NewsDetail
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name='index'),
    path('menu/',include('menu.urls')),
    path('articles/',include('article.urls')),
    path('feedback/',Feedback.as_view(),name='feedback'),
    path('contacts/',Contacts.as_view(),name='contacts'),
    path('news', NewsList.as_view(),name='news'),
    path('news/<int:pk>',NewsDetail.as_view(),name='news_detail'),
    path('login',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('registration',Registration.as_view(),name='registration'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
