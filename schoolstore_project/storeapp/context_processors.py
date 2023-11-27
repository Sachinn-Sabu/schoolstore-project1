from storeapp.models import Department, Course


def menu_links(request):
        links = Department.objects.all()

        return dict(links=links)

def sub_links(request):
        course_links = Course.objects.all()

        return dict(links=course_links)

