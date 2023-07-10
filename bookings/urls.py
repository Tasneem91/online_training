from django.urls import path
from . import views
from .views import AboutPageView, HomePageView, CaoshingPageView, ConsultantPageView
urlpatterns = [
    path('', HomePageView.as_view()),
    path('bookings/', views.index, name='all-bookings'),
    path('bookings/<slug:course_slug>/sucess', views.confirm_registration, name='confirm-registration'),
    path('bookings/<slug:course_slug>', views.courses_details, name='course-detail'),
    path("about/", AboutPageView.as_view(), name="about"),
    path("home/", HomePageView.as_view(), name="home"),
    path("consultant/", ConsultantPageView.as_view(), name="consultant"),
    path("coaching/", CaoshingPageView.as_view(), name="coaching")
]

# urlpatterns = [
#     path('', views.index, name='all-bookings'),
#     path('<slug:course_slug>/sucess', views.confirm_registration, name='confirm-registration'),
#     path('<slug:course_slug>', views.courses_details, name='course-detail')
# ]