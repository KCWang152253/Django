from django.shortcuts import render

# Create your views here.

from django.http  import HttpResponse

def index(request):
    return HttpResponse("kcwang is a good man")

def detail(request, num):
    return HttpResponse("detail-%s"%num)

from .models import Grades
def grades(request):
    # 去模版取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模版。模版再渲染页面，将渲染好的页面返回给浏览器
    return  render(request, 'myApp/grades.html', {"grades": gradesList})


from .models import Students
def students(request):
    studentsList = Students.stuObj2.all()
    return render(request, 'myApp/students.html', {"students": studentsList})

def gradesStudents(request, num):
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html', {"students": studentsList})