"""theOceanColombo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from. import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.directHome),
    url(r'^complaint1/', views.complaintFront),
    url(r'^complaint2/', views.complaintReply),
    url(r'^complaint3/', views.complaintTyping),
    url(r'^complaint4/', views.complaintCheckReply),
    url(r'^complaint5/', views.complaintUpdateReply),
    url(r'^complaint6/', views.complaintView),
    url(r'^Expenses1/', views.addExpenses),
    url(r'^Expenses2/', views.Expenseslist),
    url(r'^Expenses3/', views.AddRevenue),
    url(r'^Expenses4/', views.RevenueList),
    url(r'^Expenses5/', views.Capital),
    url(r'^Expenses6/', views.update6),
    url(r'^Expenses7/', views.ledgers),
    url(r'^Expenses8/', views.ledgersView),
    url(r'^Expenses9/', views.reports9),
    url(r'^Expenses10/', views.reportsdisplay),


]
