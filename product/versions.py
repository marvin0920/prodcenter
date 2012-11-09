# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from product import products
from product.models import Product, Version, VersionForm
from utils.message import Message, ERROR

VERSION_ROOT = "product/version/"
VERSION_FORM = VersionForm

@login_required
def home(request, page='', param=None):
    
    params = {}
    curPage = VERSION_ROOT+"home.html"
    try:
        params['products'] = Product.objects.all()
        params['versions'] = Version.objects.all()
        params['versionCreateForm'] = VERSION_FORM
    except KeyError:
        pass
    
    if page: curPage = page
    if param: params.update(param)
    return render_to_response(curPage, params,
                              context_instance=RequestContext(request))

@login_required
def list(request, prodId, page='', param=None):
    ''' list version '''
    params = {}
    curPage = VERSION_ROOT+"list.html"
    try:
        params['versions'] = Version.objects.filter(product__id__exact=prodId)
        params['versionCreateForm'] = VERSION_FORM
    except KeyError:
        pass
    
    if page: curPage = page
    if param: params.update(param)
    return products.detail(request, prodId, page=curPage, param=params)


@login_required
def detail(request, id, page='', param=None): 
    '''version detail'''
    params = {}
    curPage = VERSION_ROOT+"detail.html"
    try:
        params['version'] = get_object_or_404(Version, pk=id)
        params['versionUpdateForm'] = VERSION_FORM(instance=params['version'])
    except ValueError, KeyError:
        raise Http404
    
    if page: curPage = page
    if param: params.update(param)
    return home(request, page=curPage, param=params)

@login_required
def create(request, page='', param=None):
    '''create version'''
    params = {}
    sameVer = None
    if request.method == 'POST':
        try:
            #prodForm use modelForm
            versForm = VERSION_FORM(request.POST)
            sameVer = versForm.save()

        except ValueError, e:
            params['notice'] = Message({
                "style": "btn-danger",
                "header": "赋值错误",
                "content": "操作错误：信息新建失败！",
                "add_on": "详细信息：%s" %e
            })
            return home(request, param=params)

    return detail(request, sameVer.id, param=params)


@login_required
def update(request, id): 
    '''version update'''
    params = {}
    if request.method == 'POST':
        try:
            versObj = get_object_or_404(Version, pk=id)
            versForm = VERSION_FORM(request.POST, instance=versObj)
            sameVer = versForm.save()

        except ValueError:
            params['notice'] = Message(ERROR['duplicate'])

    return detail(request, id, param=params)


def versionMap(request):
    '''version mapping with moc'''
    curPage = VERSION_ROOT+"mapping.html"
    result = [] #result[[moc_version, [product1_vers], [product2_vers],...]]
    prodIds = request.GET.get('prods').split('_')
    prods = [Product.objects.get(pk=pid) for pid in prodIds] #product name order by prodIds
    try:
        mainVers = Version.objects.filter(product__name__exact='MOC')
        def versionMapUnit(mainVer, prodIds):
            def dependFilter(mainVer, prodId):
                subVers = Version.objects.filter(product__id__exact=prodId)
                return [subVer for subVer in subVers if subVer.depend == mainVer]
            return [mainVer]+[dependFilter(mainVer, prodId) for prodId in prodIds]
        result = [versionMapUnit(mainVer, prodIds[1:]) for mainVer in mainVers]
    except ValueError, KeyError:
        raise Http404

    params = {'prods': prods, 'result': result}
    return render_to_response(curPage, params, context_instance=RequestContext(request))

def versionSearch(request):
    curPage = VERSION_ROOT+"list.html"
    words = request.GET.get('words')

    try:
        vers = Version.objects.all()
        result = [ver for ver in vers if words in ver.__unicode__().lower()]
    except KeyError:
        raise Http404

    params = {'versions': result}
    return render_to_response(curPage, params, context_instance=RequestContext(request))




