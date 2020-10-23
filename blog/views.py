from django.db import connection
from django.shortcuts import render
from django.conf import settings
from .models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.db.models import Count
# Create your views here.

# 全局变量配置-返回函数
def global_setting(request):
   # settings中全局变量
    SITE_NAME=settings.SITE_NAME
    SITE_DESC=settings.SITE_DESC
    SITE_SINA=settings.SITE_SINA
    SITE_TENCENT=settings.SITE_TENCENT
    PRO_RSS=settings.PRO_RSS
    PRO_EMAIL=settings.PRO_EMAIL

    # 分类信息获取（导航数据）
    category_list = Category.objects.all()
    # 文章归档
    archive_list = Article.objects.distinct_date()
    # 广告数据

    # 评论排行
    comment_count_list = Comment.objects.values('article','user').annotate(comment_count=Count('article')).order_by("-comment_count")
    # comment_count_list = Comment.objects.values('article','user').annotate(Count('article'))
    # 下面为聚合函数查询结果
    # < QuerySet[{'article': 1, 'user': None, 'article__count': 1}, {'article': 2, 'user': 2, 'article__count': 1}, {'article': 3,'user': 1,'article__count': 2}] >
    # print(comment_count_list)
    article_comment_list=[Article.objects.get(pk=comment['article']) for comment in comment_count_list ]
    return locals()




def index(request):
    article_list = getPage(request, Article.objects.all())
    return render(request,'index.html',locals())
# 分页代码
def getPage(request,article_list):
    paginnator = Paginator(article_list, 1)
    try:
        # 得到页码对象，没传默认返回1
        page=int(request.GET.get('page',1))
        # 分页对象获取页面数据
        article_list=paginnator.page(page)
    except (EmptyPage,InvalidPage,PageNotAnInteger):
        # 异常错误默认返回第1页
        article_list=paginnator.page(1)
    return article_list
# 归档数据
def archive(request):
    year=request.GET.get('year',None)
    month=request.GET.get('month',None)
    article_list = Article.objects.filter(date_publish__icontains=year + '-' + month)
    article_list=getPage(request,article_list)
    print(year,month)
    return render(request, 'archive.html', locals())
