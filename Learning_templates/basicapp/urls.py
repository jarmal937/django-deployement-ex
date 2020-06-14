from django.urls import path
from basicapp import views
app_name="basicapp"

urlpatterns=[
    path('relative/',views.relative_urls_templates,name="relative_urls_templates"),
    path('other/',views.other,name="other"),
 ]
