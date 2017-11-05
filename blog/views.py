#coding:utf8
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from blog.models import Blog,Comment,Statistics
from django.http import JsonResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core import serializers
import json,redisCache,os

def login(request):

    try:
        state = request.session['state']
    except KeyError,e:
        state = 'success'

    return render(request,"login.html",{state:"Error!!!!"})

def loginVerify(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username,password=password)
    if user:
        auth.login(request,user)
        request.session['user']=username
        data = Blog.objects.all().values()
        #return render(request,'blogList.html',{'username':request.session['user'],'blogList':data})
        return HttpResponseRedirect('/blogList')
    else:
        request.session['state'] = 'error'
        return HttpResponseRedirect('/login',{'error':"Error!!!!"})

# def blogList(request):
#     data = Blog.objects.all().values()
#     paginter = Paginator(data,2)
#     page = request.GET.get('page')
#     print "test"
#     try:
#         cus = paginter.page(page)
#         print "*"*50
#         print cus
#     except PageNotAnInteger:
#         cus = paginter.page(1)
#     except EmptyPage:
#         cus = paginter.page(paginter.num_pages)
#     return render(request, 'blogList.html', {'username': request.session['user'], 'blogList': cus})

def blogList(request):
    page = request.GET.get('page')
    if not page:
        page=0
    else:
        page=int(page)-1
    totalData = Blog.objects.all().values()
    pageShow = totalData[3*page:3*(page+1)]
    return render(request, 'blogList.html', {'username': request.session['user'], 'blogList': pageShow,'page':totalData})


def blogError(request):
    return render(request, 'login.html', {'error': "Error!!!!"})

@login_required
def addBlog(request):

    return render(request,'addBlog.html')

@login_required
def saveBlog(request):
    data = Blog.objects.all().values()
    try:
        user = request.session.get('user')
        r_title = request.POST.get('title')
        r_content = request.POST.get('content')
        blog = Blog.objects.create(title=r_title,content=r_content,like=0,unlike=0)
        #blog.save()
        #return render(request, 'blogList.html', {'username': request.session['user'], 'blogList': data})
        return HttpResponseRedirect('/blogList')
    except Exception,e:
        print e
        return HttpResponseRedirect('/error')



#
# def blog(request,blogid):
#     data = Blog.objects.get(id=blogid)
#     title = data.title
#     content = data.content
#     like = data.like
#     unlike = data.unlike
#     return render(request,'viewBlog.html',{'id':blogid,'title':title,'content':content,'like':like,'unlike':unlike})



def ajax_like(request,blogid):
    data = redisCache.read_from_cache(blogid)
    like = data.like
    # data = Blog.objects.get(id=blogid)
    # like = data.like
    # like = int(like)+1
    # data.like = like
    # data.save()
    like = int(like)+1
    print "?????"
    data.like = like
    redisCache.write_to_cache(blogid, data)
    return JsonResponse({'like':str(like),'message':u'点赞成功'},safe=True)

def ajax_unlike(request,blogid):
    data = Blog.objects.get(id=blogid)
    unlike = data.unlike
    unlike = int(unlike)+1
    data.unlike = unlike
    data.save()
    return JsonResponse({'unlike':str(unlike),'message':u'拍砖成功'},safe=True)


# def test(request):
#     return render(request,'addBlog.html')


def blog(request,blogid):
    # data = Blog.objects.get(id=blogid)
    data = redisCache.read_from_cache(blogid)

    comments = Comment.objects.filter(blog_id=blogid)
    statistics = Statistics.objects.filter(blog_id=blogid)
    if not statistics:
        Statistics.objects.create(blog_id_id=blogid)
        statistics = Statistics.objects.filter(blog_id=blogid)
    vister = statistics[0].view+1
    statistics.update(view=vister)
    username = request.session['user']

    comments_count = comments.__len__()
    return render(request,'article.html',{'data':data.like,'comments':comments,'username':username,'vister':vister,'comments_count':comments_count})

def track(request):
    images_all = []
    images = os.listdir('D:\\web\\myBlog\\blog\\static\\blog\\image')
    for image in images:
        print image
        print type(image)
        images_all.append(image)
        # print image

    return render(request,'trackingTest.html',{'images':iamges_all})


def addComment(request):
    try:
        # data = Comment.object.get(id=blogid)
        # username = request.session.get('user')
        username = request.session.get('user')
        blogid = request.GET.get('blogid')
        comment = request.GET.get('comment')
        blogid = Blog.objects.get(id = int(blogid))
        Comment.objects.create(blog_id=blogid,content=comment,username = username)
        # res.save()
        comments = 0
        try:
            statistics = Statistics.objects.get(blog_id=blogid)
            statistics.comments = statistics.comments + 1
            comments = statistics.comments
            statistics.save()
        except Statistics.DoesNotExist:
            Statistics.objects.create(view=0,comments=1,blog_id_id=int(request.GET.get('blogid')))
            comments = 1


        return JsonResponse({'message':u'提交评论成功','comments':comments},safe=True)
    except Exception,e:
        print e
        return JsonResponse({'message':u'提交失败'},safe=True)

def getComment(request):
    blogid = request.GET.get('blogId')
    # print request.session.get('user')
    comments = Comment.objects.filter(blog_id=blogid)
    # username = request.session.get('user')
    # return JsonResponse({'comments':comments,'message':'success'},safe=True)
    # return render(request,'getComment.html',{'comments':comments,'username':username})
    return render(request, 'getComment.html', {'comments': comments})

def getCommentJson(request):
    blogid = request.GET.get('blogId')
    comments = Comment.objects.filter(blog_id=blogid)
    # username = 'Tom'
    # return JsonResponse(json.dumps({'comments':comments,'message':'success'}),safe=True)
    # return JsonResponse(comments,safe=True)
    json_comments = serializers.serialize('json',comments)
    return HttpResponse(json_comments,content_type='application/json')


def test(request):

    obj_list = ['page01','page02','page03','page04','page05','page06','page07','page08','page09','page10',
                'page11','page12','page13','page14','page15','page16','page17','page18','page19','page20',
                'page21','page22','page23','page24','page25','page26','page27','page28','page29','page30',]
    #create a paginator instance
    paginator = Paginator(obj_list,1)

    #Get the page_number of current page
    current_page_num = request.GET.get('page')

    try:
        current_page = paginator.page(current_page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        current_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        current_page = paginator.page(paginator.num_pages)
    return render(request,'test.html',
                  {'current_page': current_page,
                   'paginator': paginator

                  })



# Create your views here.
