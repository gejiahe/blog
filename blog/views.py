from django.db import connection
from django.shortcuts import render
from django.conf import settings
from .models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
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
    return locals()


def index(request):
    # 最新文章数据
    # article_list=Article.objects.all()
    article_list = getPage(request, Article.objects.all())
    # 分页 -> 分页对象
    # paginnator=Paginator(article_list,1)
    # 文章归档数据
    # 1. cursor.execute 方法执行sql
    # select_sql="SELECT DISTINCT DATE_FORMAT(date_publish,'%Y-%m') as col_date FROM blog_article ORDER BY date_publish"
    # select_sql="SELECT DISTINCT date_publish as col_date FROM blog_article ORDER BY date_publish"
    # cursor=connection.cursor()
    # cursor.execute(select_sql)
    # archive_list=cursor.fetchall()

    # 2. raw 方法执行SQL
    # select_sql="SELECT DISTINCT DATE_FORMAT(date_publish,'%%Y-%%m') as col_date,id FROM blog_article ORDER BY date_publish"
    # archive_list=Article.objects.raw(select_sql)
    # print(archive_list)
    # 3.使用自定义模型管理器类方法
    # archive_list=Article.objects.distinct_date()
    # try:
    #     # 得到页码对象，没传默认返回1
    #     page=int(request.GET.get('page',1))
    #     # 分页对象获取页面数据
    #     article_list=paginnator.page(page)
    # except (EmptyPage,InvalidPage,PageNotAnInteger):
    #     # 异常错误默认返回第1页
    #     article_list=paginnator.page(1)
    return render(request,'index.html',locals())
# 分页代码
def getPage(request,article_list):
    paginnator = Paginator(article_list, 2)
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
    print(year,month)
    # article_list=Article.objects.filter(date_publish__icontains=year+'-'+month)
    article_list = Article.objects.filter(date_publish__icontains=year + '-' + month)
    article_list=getPage(request,article_list)
    return render(request, 'archive.html', locals())
