from django.shortcuts import render
from django.conf import settings
from .models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
# Create your views here.

# 全局变量配置-返回函数
def global_setting(request):
    return {
    "SITE_NAME":settings.SITE_NAME,
    "SITE_DESC":settings.SITE_DESC,
    "SITE_SINA" : settings.SITE_SINA,
    "SITE_TENCENT" :settings.SITE_TENCENT,
    "PRO_RSS" :settings.PRO_RSS,
    "PRO_EMAIL":settings.PRO_EMAIL,
    }

def index(request):
    # 分类信息获取（导航数据）
    category_list=Category.objects.all()
    # 广告数据
    # 最新文章数据
    article_list=Article.objects.all()
    # 分页 -> 分页对象
    paginnator=Paginator(article_list,1)
    try:
        # 得到页码对象，没传默认返回1
        page=int(request.GET.get('page',1))
        # 分页对象获取页面数据
        article_list=paginnator.page(page)
    except (EmptyPage,InvalidPage,PageNotAnInteger):
        # 异常错误默认返回第1页
        article_list=paginnator.page(1)
    return render(request,'index.html',{'category_list':category_list,'article_list':article_list})
