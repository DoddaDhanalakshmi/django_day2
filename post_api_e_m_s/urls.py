from django.urls import path
from .views import create_emp,addingemp,getallemp
urlpatterns=[
    path("",create_emp),
    path("api/add/emp",addingemp,name="creation"),
    path("api/getallemp",getallemp,name="getemp")
]