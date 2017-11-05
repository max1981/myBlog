"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views as blogViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
url(r'^login/$', blogViews.login,name="login"),
url(r'^loginVerify$', blogViews.loginVerify,name="loginVerify"),
url(r'^addBlog/$', blogViews.addBlog,name="addBlog"),
url(r'^saveBlog/', blogViews.saveBlog,name="save"),
url(r'^blog/([0-9]+)/$', blogViews.blog,name="blog"),
url(r'^ajaxlike/([0-9]+)/$', blogViews.ajax_like,name="ajax_like"),
url(r'^blogList/$', blogViews.blogList,name="blogList"),
url(r'^ajaxunlike/([0-9]+)/$', blogViews.ajax_unlike,name="ajax_unlike"),
url(r'^error/$', blogViews.blogError,name="error"),
# url(r'^bootstrapTest/([0-9]+)/$', blogViews.bootstrapTest,name="bootstrapTest"),
url(r'^addComment/$', blogViews.addComment,name="addComment"),
url(r'^track/$', blogViews.track,name="track"),
url(r'^getComment/$', blogViews.getComment,name="getComment"),
url(r'^getCommentJson/$', blogViews.getCommentJson,name="getCommentJson"),
url(r'^getComment/([0-9]+)/$', blogViews.getComment,name="getComment"),

url(r'^test$', blogViews.test,name="test"),
]
