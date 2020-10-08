from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from django.template.loader import get_template
from django.shortcuts import redirect
# Create your views here.
def homepage(request):
    template=get_template('index.html')
    posts =Post.objects.all()
    now =datetime.now()
    html=template.render(locals())
    return HttpResponse(html)


    # posts=Post.objects.all()
    # posts_lists=list()
    # for count,post in enumerate(posts):
    #     posts_lists.append("NO.{}:".format(str(count))+str(post)+"<br>")
    # return HttpResponse(posts_lists)
def showpost(request,slug):
    template=get_template('post.html')
    try:
        post=Post.objects.get(slug=slug)
        now = datetime.now()
        if post != None:
            html=template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')