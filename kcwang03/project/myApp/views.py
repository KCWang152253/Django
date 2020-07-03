from django.shortcuts import render

# Create your views here.

from django_redis import get_redis_connection
# conn = get_redis_connection("default")

from django.views.decorators.cache import cache_page

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


from .models import Students, Grades
def students(request):
    studentsList = Students.stuObj2.all()
    return render(request, 'myApp/students.html', {"students": studentsList})

def students2(request):
    # 查询单一数据出现多条结果时报异常
    studentList = Students.stuObj2.get(sgender=True)
    return HttpResponse("``````````````")


# 显示前2条学生
def students3(request):
    studentsList = Students.stuObj2.all()[0:2]
    return render(request, 'myApp/students.html', {"students": studentsList})

# 分页显示学生
def stupage(request,page):

    page = int(page)
    studentsList = Students.stuObj2.all()[(page-1)*2:page*2]
    return render(request, 'myApp/students.html', {"students": studentsList})

from django.db.models import  Max
def studentsearch(request):
    studentsList = Students.stuObj2.filter(sname__contains="成")
    # studentsList = Students.stuObj2.filter(sname__startswith="吴")
    # studentsList = Students.stuObj2.filter(pk__in=[2,4])
    # gt大于，gte大于等于, lt小于， lte小于等于
    # studentsList = Students.stuObj2.filter(sage__gt=5)
    # studentsList = Students.stuObj2.filter(lastTime__year=2017)
    maxAge = Students.stuObj2.aggregate(Max('sage'))
    print(maxAge)


    return render(request, 'myApp/students.html', {"students": studentsList})



def gradesStudents(request, num):
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html', {"students": studentsList})

def addstudent(request):
    grade = Grades.objects.get(pk=2)
    stu = Students.createStudent("刘德华",34,True,"我叫刘德华01,请多关照",grade,"2018-3-9","2018-4-6")
    stu.save()
    return  HttpResponse("kcwang0000")


def addstudent2(request):
    grade = Grades.objects.get(pk=2)
    stu = Students.stuObj2.createStudent("张学友",34,True,"我叫张学友,请多关照",grade,"2018-3-9","2018-4-6")
    stu.save()
    return  HttpResponse("kk0000")


from  django.db.models import  F,Q
# F对象
def grades(request):
    g = Grades.objects.filter(ggirlnum__lt=F('gboynum'))
    print(g)
    return  HttpResponse("0000000003333")


# 获取request的对象属性
def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribles")

# get获取浏览器传递给服务器的数据get1?a=1&a=2&c=3

def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a+"   "+b+"   "+c)

def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1+"   "+a2+"   "+c)

# POST
def showregist(request):
    return render(request,'myApp/regist.html')


def regist(request):
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.get("hobby")



    print(name)
    print(gender)
    print(age)
    print(hobby)

    return HttpResponse("我是可控")

def showresponse(requseat):
    res = HttpResponse()
    res.content = b'good'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    # print(res.content-type)
    return res
# cookie测试
def cookietest(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write("<h1>"+cookie["kcwang"]+"</h1>")
    # cookie = res.set_cookie("kcwang","good")
    return res

# 重定向
from  django.http import HttpResponseRedirect ,JsonResponse
from  django.shortcuts import redirect
def redirect1(request):
    # return HttpResponseRedirect('/redirect2')
    return redirect('/redirect2')
def redirect2(request):
    return HttpResponse("我是重定向后的视图")
    # if request.is_ajax():
    #     a = JsonResponse({})
    # return a


# session 服务器接收http请求后，会根据报文创建HttpRequest对象，然后将这个对象传给视图的第一个参数request，这个对象通常是Django形成的
# 客户端与服务端的一次通信就是一次会话，为实现状态保持，在客户端或者服务端会存储有关会话的数据，session所有的数据储存在服务端，不同的请求者之间不会共享这个数据，
# 在启用session后，每个Httprequest对象都有一个request属性，
def main(request):
    # 取session

    username = request.session.get('name', "游客")
    print(username)
    return render(request, 'myApp/main.html', {'username':username})

def login(request):
    return render(request, 'myApp/login.html')

def showmain(request):
    username = request.POST.get('username')
    # 存储session
    request.session['name']= username
    print(username, username)
    request.session.set_expiry(5)
    return redirect('/main')

from django.contrib.auth import logout
def quit(request):
    # 清除session
    logout(request)
    # request.session.clear()  清空所有的会话
    # request.session.flush()  删除当前的会话，并且删除会话的cookie


    return redirect('/main/')


# def set_session(request):
#     """"保存session数据"""
#
#     request.session['username'] = 'Django'
#     request.session['verify_code'] = '123456'
#     return HttpResponse('保存session数据成功')
#
# def get_session(request):
#     """获取session数据"""
#
#     username = request.session.get('username')
#     verify_code = request.session.get('verify_code')
#     text = 'username=%s, verify_code=%s' % (username, verify_code)
#     return HttpResponse(text)
#
#
# def get1(request):
#         # from redis import StrictRedis  # 原生redis
#         # sr = StrictRedis(host='172.0.0.1', port='6379', db=9)
#
#         # 通过Django-redis获取StrictRedis对象。(需要在settings.py中配置redis的链接)
#     con = get_redis_connection('default')  # con就是StrictRedis类型。default对应settings.py中CACHES中设置的default。
#     result = con.set('321', '张三')  # redis中存储String
#
#     return HttpResponse('ok')


#  生成验证码的图片，也可以用第三方库生成
def verifycode(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景颜色，宽，高
    bgcolor = (random.randrange(20,100), random.randrange(20,100),random.randrange(20,100))
    width = 100
    height = 50
    # 创建画面对象
    im = Image.new('RGB',(width,height),bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0,100):
        xy = (random.randrange(0,width),random.randrange(0,height))
        fill = (random.randrange(0,255), 255, random.randrange(0,255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0,4):
        rand_str += str[random.randrange(0,len(str))]
    # 构造字体颜色
    font = ImageFont.truetype(r'/System/Library/Fonts/Songti.ttc',40)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0,255),random.randrange(0,255))
    # 绘制4个字
    draw.text((5,2),rand_str[0],font=font,fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session ,用于进一步做验证



    request.session['verify'] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片存入内存中，文件类型为png
    im.save(buf,'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

from django.shortcuts import render,redirect

def verifycodefile(request):
    f = request.session.get("flag",True)
    str = ""
    if f == False:
        str = "请重新输入"
    request.session.clear()
    return render(request, 'myApp/verifycodefile.html', {"flag":str})


def verifycodecheck(request):
    code1 = request.POST.get("verifycode").upper()
    code2 = request.session["verify"].upper()
    if code1 == code2:
        return render(request,'myApp/success.html')
    else:
        request.session["flag"] = False
        return redirect('/verifycodefile/')


