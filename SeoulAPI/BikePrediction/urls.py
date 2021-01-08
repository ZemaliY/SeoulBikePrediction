from django.conf.urls   import url
from BikePrediction import views

urlpatterns = [
    url(r'predict/$'              , views.predict),
    url(r'^locations/$'               , views.location_list  ),
    url(r'^location/(?P<pk>[0-9]+)/$' , views.location_detail),
]