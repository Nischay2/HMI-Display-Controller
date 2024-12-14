from django.contrib import admin
from django.urls import path, include

from server.views import TextView


urlpatterns = [
    # path('api/status/', StatusPost.as_view(), name='status'),
    path('text/', TextView.as_view(), name='text')
    


]