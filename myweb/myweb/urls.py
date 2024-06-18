from django.contrib import admin
from django.urls import path, include

# def home(request):
#     print(request)
#     return HttpResponse("<h1>hi there</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home),
    path('', include('base.urls')),
]
