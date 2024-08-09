from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# HTTP REQUEST
def my_view(request):
    return HttpResponse("UMA LINDA STRING")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_view)
]
