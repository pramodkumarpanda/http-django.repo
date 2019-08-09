#from django.urls import path
from django.conf.urls import url
from .views import HomePageView, AboutPageView,PostPageView

urlpatterns = [
    url('^$', HomePageView.as_view(), name='home'),
    url('^about/$', AboutPageView.as_view(), name='about'),
    url('^posts/$',PostPageView.as_view(), name='posts'),
]
