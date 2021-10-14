from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('timetable.urls')),
    # path('showtable/',include('timetable.urls')),
    # path('adminpanel/',include('timetable.urls')),
    # path('login/', include('timetable.urls')),
    # path('submit/',include('timetable.urls')),
    # path('logout/', include('timetable.urls')),
]
