from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from storeapp.models import Department, Course


# Create your views here.
def home(request):
    return render(request, 'home.html')


def allDept(request, d_slug=None):
    d_page = None
    product_list = None

    if d_slug is not None:
        d_page = get_object_or_404(Department, slug=d_slug)
        courses = Course.objects.filter(department=d_page)
    else:
        courses = Course.objects.all()

    return render(request, 'home.html', {'department': d_page, 'course': courses})

def user(request):
    return render(request, 'user.html')


def form(request):
    if request.method == 'GET':
        # This is when the form is initially loaded
        departments = Department.objects.all()
        return render(request, 'form.html', {'departments': departments})
    elif request.method == 'POST':
        # Handle form submission if needed
        # You may need to process the form data, save it to the database, etc.
        # After processing, redirect to the appropriate page
        return redirect('storeapp:home')


def get_courses_by_department(request):
    department_id = request.GET.get('department', None)

    if department_id is not None:
        department = get_object_or_404(Department, id=department_id)
        courses = Course.objects.filter(department=department).values('id', 'name')
    else:
        courses = Course.objects.all().values('id', 'name')

    return JsonResponse({'courses': list(courses)})
def confirm(request):
    return render(request, 'confirmation.html')

