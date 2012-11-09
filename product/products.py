# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from product.models import Product, ProductForm, FunctionForm
from utils.message import Message, ERROR

PRODUCT_ROOT = "product/"
PRODUCT_FORM = ProductForm
FUNCTION_FORM = FunctionForm

@login_required
def home(request, page='', param=None):
    
    params = {}
    curPage = PRODUCT_ROOT+"home.html"
    try:
        params['products'] = Product.objects.all()
        params['productCreateForm'] = PRODUCT_FORM()
    except KeyError:
        pass
    
    if page: curPage = page
    if param: params.update(param)
    return render_to_response(curPage, params,
                              context_instance=RequestContext(request))

@login_required
def create(request):
    '''info model has been created here'''
    params = {}
    sameProds = None
    if request.method == 'POST':
        try:
            #prodForm use modelForm
            prodForm = PRODUCT_FORM(request.POST) 
            sameProds = prodForm.save()
            # if sameProds[0]:
            #     return redirect(sameProds[1]) # prodForm.get_absolute_url() will be called

        except ValueError, e:
            params['notice'] = Message({
              "style": "btn-danger",
              "header": "赋值错误",
              "content": "操作错误：信息新建失败！",
              "add_on": "详细信息：%s" %e
            })
    
    return detail(request, sameProds[1], param=params)

@login_required
def detail(request, id, page='', param=None): 
    '''product detail'''
    params = {}
    curPage = PRODUCT_ROOT+"detail.html"
    try:
        params['product'] = get_object_or_404(Product, pk=id)
        params['productUpdateForm'] = PRODUCT_FORM(instance=params['product'])
        params['functionCreateForm'] = FUNCTION_FORM()
    except ValueError, KeyError:
        raise Http404

    if page: curPage = page
    if param: params.update(param)
    return home(request, page=curPage, param=params)

@login_required
def update(request, id): 
    '''product update'''
    params = {}
    if request.method == 'POST':
        try:
            prodObj = get_object_or_404(Product, pk=id)
            prodForm = PRODUCT_FORM(request.POST, instance=prodObj)
            sameProds = prodForm.save()
            if not sameProds[0]:
                params['notice'] = Message(ERROR['duplicate'])
        except ValueError:
            raise Http404

    return detail(request, id, param=params)