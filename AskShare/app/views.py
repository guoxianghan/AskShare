#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from app import check_code
from io import BytesIO
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
#写在这个位置吗 
    list1 = ['physics', 'chemistry', 1997, 2000]
    return render(
        request,
        'app/index.html',
        {
            'arr':list1,
            'title':'AskShare',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def register(request):
    """Renders the about page."""
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/account/register.html',
        {
             'title':'http://localhost:60122/',
        }
    )
def register_post(request):
    assert isinstance(request,HttpRequest)
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)

def create_code_img(request):
    f = BytesIO() #直接在内存开辟一点空间存放临时生成的图片
    img, code = check_code.create_validate_code() #调用check_code生成照片和验证码
    request.session['check_code'] = code #将验证码存在服务器的session中，用于校验
    try:
      img.save(f,'PNG') #生成的图片放置于开辟的内存中
    except Exception,e:
        return HttpResponse(e.message)
    return HttpResponse(f.getvalue())  #将内存的数据读取出来，并以HttpResponse返回