from django.conf.urls import url
from my_app.views import dashboard_views

urlpatterns = [
    url(r'^$', dashboard_views.index_dashboard, name="index"),
]