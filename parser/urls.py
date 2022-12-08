from django.urls import path
from .views import ProductView, upload_file

urlpatterns = [
    path('', upload_file, name='upload'),
    path('view/', ProductView.as_view(), name='view'),

]
