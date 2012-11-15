# -*- coding: utf-8 -*-
__author__ = 'marvin'
import sys
reload(sys)
sys.setdefaultencoding('utf8')


from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import Http404
from known.models import Article, ArticleForm
from known.utils import listing, Message, ERROR, STATIC


KNOWN_ROOT = "known/"
ARTICLE_FORM = ArticleForm

#@login_required
def home(request, pageNum=1, articles=None, page='', param=None):

    params = {}

    if not(articles or page):
        try:
            articles = Article.objects.all()
        except KeyError:
            raise Http404


    articles = articles.filter(status__exact=1)

    params['folders'] = STATIC['FOLDER']
    params['topArticles'] = articles.exclude(folder__iexact='notice').order_by('-count')[:10]
    params['topNotices'] = articles.filter(folder__iexact='notice').order_by('-created')[:10]

    articles.exclude(folder__iexact='notice')

    curPage = KNOWN_ROOT+"home.html"
    if page: curPage = page
    if param: params.update(param)
    return listing(request, curPage, params,allObjects=articles, pageNum=pageNum)

@login_required
def space(request, pageNum=1, articles=None, page='', param=None):
    params = {}
    if not(articles or page):
        try:
            articles = Article.objects.all()
        except KeyError:
            raise Http404

    articles = articles.filter(author=request.user)
    params["where"] = "space"
    curPage = KNOWN_ROOT+"space.html"
    if page: curPage = page
    if param: params.update(param)
    return listing(request, curPage, params,allObjects=articles, pageNum=pageNum)

@login_required
def createArticle(request, page='', param=None):

    params = {}
    if request.method == 'GET':
        curPage = KNOWN_ROOT+"createArticle.html"
        params['articleCreateForm'] = ARTICLE_FORM()
        params["where"] = "create"
        return render_to_response(curPage, params, context_instance=RequestContext(request))

    if request.method == "POST":
        try:
            articleForm = ARTICLE_FORM(request.POST)
            newArticle = articleForm.save(commit=False)

            newArticle.author = request.user
            newArticle.count = 0
            newArticle.save()

        except ValueError, e:
            params['notice'] = Message({
                "style": "btn-danger",
                "header": "赋值错误",
                "content": "操作错误：信息新建失败！",
                "add_on": "详细信息：%s" %e
            })
            return redirect("/known/article/create/")
    return redirect("/known/space/")

def detailArticle(request, id, page='', param=None):

    params = {}
    curPage = KNOWN_ROOT+"detailArticle.html"
    try:
        newArticle = get_object_or_404(Article, pk=id)
        newArticle.count += 1
        newArticle.save()
        params['article'] = newArticle

    except ValueError:
        raise Http404

    if page: curPage = page
    if param: params.update(param)
    return home(request, page=curPage, param=params)

@login_required
def updateArticle(request, id, page='', param=None):
    '''article update'''
    params = {}
    if request.method == 'GET':
        newArticle = get_object_or_404(Article, pk=id)
        params['article'] = newArticle
        params['articleUpdateForm'] = ARTICLE_FORM(instance=newArticle)
        curPage = KNOWN_ROOT+"updateArticle.html"
        return render_to_response(curPage, params, context_instance=RequestContext(request))
    if request.method == 'POST':
        try:
            article = get_object_or_404(Article, pk=id)
            articleForm = ARTICLE_FORM(request.POST, instance=article)
            newArticle = articleForm.save()

        except ValueError:
            params['notice'] = Message(ERROR['duplicate'])
            return updateArticle(request, id, param=params)

    return redirect("/known/article/%s/detail/" %id)

@login_required
def deleteArticle(request, id, page='', param=None):

    params = {}
    try:
        article = get_object_or_404(Article, pk=id)
        article.delete()
    except KeyError:
        raise Http404
    return redirect("/known/space/")


def listByFolder(request, folder, pageNum=1, page='', param=None):
    params = {}
    curPage = KNOWN_ROOT+"home.html"
    try:
        articles = Article.objects.exclude(status__iexact=0).filter(folder__iexact=folder)
    except KeyError:
        raise Http404

    if page: curPage = page
    if param: params.update(param)
    return home(request, articles=articles, pageNum=pageNum, page=curPage, param=params)



def listByStatus(request, status, pageNum=1, page='', param=None):
    params = {}
    curPage = KNOWN_ROOT+"space.html"
    try:
        articles = Article.objects.filter(status__exact=status)
    except KeyError:
        raise Http404

    if page: curPage = page
    if param: params.update(param)
    return space(request, articles=articles, pageNum=pageNum, page=curPage, param=params)