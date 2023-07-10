from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course, Participant
from .forms import RegistrationForm
from django.views.generic import TemplateView
# Create your views here.
def index(request):
    # bookings = [
    #     {
    #         'title': 'Python Beginner to Advance',
    #         'location': 'Tianjin',
    #         'slug': 'tianjin-beginner-python-course'
    #     },
    #     {
    #         'title': 'Python OOP',
    #         'location': 'Beijing',
    #         'slug': 'beijing-oop-python-course'
    #     },
    #     {
    #         'title': 'Django Framework',
    #         'location': 'Guangzhou',
    #         'slug': 'guangzhou-django-python-course'
    #     }
    # ]
    bookings = Course.objects.all()


    return render(request, 'bookings/index.html', {
        'bookings': bookings
    })
    # return HttpResponse('Hello World')


def courses_details(request, course_slug):
    try:
        selected_course = Course.objects.get(slug=course_slug)
        if request.method == "GET":

            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_course.participant.add(participant)
                return redirect('confirm-registration', course_slug=course_slug)

        return render(request, 'bookings/course-details.html', {
            'course_found': True,
            'course': selected_course,
            'form': registration_form
            # 'course_title': selected_course.title,
            # 'course_description': selected_course.description
        })
    except Exception as e:
        return render(request, 'bookings/course-details.html',{
            'course_found' : False
        })


def confirm_registration(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    return render(request, 'bookings/registration-success.html', {
        'organizer_email': course.organizer_email
    })

class AboutPageView(TemplateView):  # new
    template_name = "bookings/about.html"


class HomePageView(TemplateView):
    template_name = "bookings/home.html"

class CaoshingPageView(TemplateView):
    template_name = "bookings/caoshing.html"

class ConsultantPageView(TemplateView):
    template_name = "bookings/consultant.html"







