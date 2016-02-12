from django.conf.urls import url
from .views import LogIn, PanelView

urlpatterns = [
    # url(r'^$', Index.as_view(), name="Index"),
    url(
        r'^login/$',
        LogIn.as_view(),
        name="login"
    ),
    url(
        r'^salir/$',
        'apps.users.views.LogOut',
        name="logout"
    ),
    url(
        r'^panel/$',
        PanelView.as_view(),
        name="Panel"
    ),
]
