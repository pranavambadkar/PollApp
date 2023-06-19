from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles import views
from pollapp.views import uhome, create, ulogin, usignup, ulogout, demo, demoresult, about, vote, viewpoll, results, deletepoll, confirm, ucp

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", uhome, name = "uhome"),
    path("create", create, name = "create"),
    path("demo", demo, name = "demo"),
    path("demoresult", demoresult, name="demoresult"),
    path("about", about, name = "about"),
    path("ulogin", ulogin, name = "ulogin"),
    path("usignup", usignup, name = "usignup"),
    path("ulogout", ulogout, name = "ulogout"),
    path("viewpoll", viewpoll, name = "viewpoll"),
    path("vote/<poll_id>", vote, name = "vote"),
    path("results/<poll_id>", results, name = "results"),
    path("deletepoll/<poll_id>", deletepoll, name = "deletepoll"),
    path("confirm/<poll_id>", confirm, name="confirm"),
    path("ucp", ucp, name="ucp"),
    path('favicon.ico', views.serve, {'path': 'favicon.ico'}),
]
