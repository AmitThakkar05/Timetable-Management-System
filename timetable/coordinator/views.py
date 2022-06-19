from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import courseTable

# Create your views here.
def coordinatorPage(request):
    template = loader.get_template('coordinatorPage.html')
    return HttpResponse(template.render())

#### COURSES PAGES ####
def course(request):
    courseDetails = courseTable.objects.all().values()
    template = loader.get_template('courses.html')
    context = {
        'allCourses' : courseDetails,
    }
    return HttpResponse(template.render(context, request))

def addCourse(request):
    template = loader.get_template('addCourse.html')
    return HttpResponse(template.render({}, request))

def courseRecord(request):
    course_id = request.POST.get('courseID')
    course_name = request.POST.get('courseName')
    course_credit = request.POST.get('credit')
    course_batch = request.POST.get('batch')


    # courseID courseName credit  batch 
    curCourse = courseTable(courseID=course_id, courseName=course_name, credit=course_credit, batch = course_batch)
    curCourse.save()

    return HttpResponseRedirect(reverse('course'))

def deleteCourse(request, id):
    curCourse = courseTable.objects.get(id=id)
    curCourse.delete()
    return HttpResponseRedirect(reverse('course'))





#### BATCHES PAGES####

def batch(request):
    # courseDetails = courseTable.objects.all().values()
    template = loader.get_template('batches.html')
    # context = {
        # 'allCourses' : courseDetails,
    # }
    # return HttpResponse(template.render(context, request))
    return HttpResponse(template.render())