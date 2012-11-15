# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from product.models import Function, FunctionForm
from utils.message import Message, ERROR

FUNCTION_ROOT = "product/function/"
FUNCTION_FORM = FunctionForm

@login_required
def create(request):
    '''create function'''
    
    if request.method == 'POST':
        params = {}
        sameFuncs = None
        try:
            #funcForm use modelForm
            funcForm = FUNCTION_FORM(request.POST) 
            sameFuncs = funcForm.save()

        except ValueError, e:
            params['notice'] = Message({
              "style": "btn-danger",
              "header": "赋值错误",
              "content": "操作错误：信息新建失败！",
              "add_on": "详细信息：%s" %e
            })
        return detail(request, sameFuncs.id, param=params)
    
    

@login_required
def detail(request, id, page='', param=None):
    '''function detail'''
    params = {}
    curPage = FUNCTION_ROOT+"detail.html"
    try:
        params['function'] = get_object_or_404(Function, pk=id)
        params['functionUpdateForm'] = FUNCTION_FORM(instance=params['function'])
    except ValueError, KeyError:
        raise Http404

    if page: curPage = page
    if param: params.update(param)
    return render_to_response(curPage, params,
                              context_instance=RequestContext(request))

@login_required
def update(request, id): 
    '''product update'''
    
    if request.method == 'POST':
        params = {}
        try:
            funcObj = get_object_or_404(Function, pk=id)
            funcForm = FUNCTION_FORM(request.POST, instance=funcObj)
            sameFuncs = funcForm.save()
#            if not sameFuncs[0]:
#                params['notice'] = Message(ERROR['duplicate'])
        except ValueError:
            raise Http404
        return detail(request, id, param=params)

    if request.method == 'GET':
        page = FUNCTION_ROOT+'create.html'
        param = {'functionUpdateForm': FUNCTION_FORM()}
        return render_to_response(page, param,
                              context_instance=RequestContext(request))