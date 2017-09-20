"""project_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from library import views as library_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',library_view.index),
    url(r'^getbook/',library_view.get_books),
    url(r'^getbookbyid/',library_view.get_bookby_id),
    url(r'^getbooksByUser/',library_view.get_booksByUsers),
    url(r'^get_user_details/',library_view.get_user_details),
    url(r'^login/',library_view.login),
    url(r'^register/',library_view.register),
    url(r'^profile/',library_view.profile),
    url(r'^insertbook/',library_view.insert_book),
    url(r'^logout/',library_view.logout),
    url(r'^insertbookform/',library_view.insert_book_form)

]
