from django.urls import path

from prayers.api import views


urlpatterns =[
    path('customprayers/', views.CustomPrayersCreateAPIView.as_view()),
    path('prayerrequests/',views.CustomPrayerAPIView.as_view()),
    path('requestedprayers/', views.PrayersRequestedAPIView.as_view())
]