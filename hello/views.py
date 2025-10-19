from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    """简单的Hello World视图"""
    return HttpResponse("<h1>20231201063 龙娇 🎉</h1><p>欢迎来到2023医疗项目！</p>")

def hello_name(request, name):
    """带参数的Hello视图"""
    return HttpResponse(f"<h1>20231201063 龙娇 - {name}! 👋</h1><p>很高兴见到你！</p>")

def hello_template(request):
    """使用模板的Hello视图"""
    context = {
        'title': '20231201063 龙娇',
        'message': '这是一个使用模板的Hello World页面！',
        'features': ['Django框架', 'Python语言', 'Web开发'],
        'student_info': '20231201063 龙娇'
    }
    return render(request, 'hello/index.html', context)
