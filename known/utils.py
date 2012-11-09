# -*- coding: utf-8 -*-

__author__ = 'marvin'

STATIC = {
    'STATUS': (('0', '草稿'),
               ('1', '发布')
        ),
    'FOLDER': (('unknown', '未分类'),
               ('notice', '部门公告'),
               ('testFunction', '功能测试'),
               ('testTheory', '测试理论'),
               ('testAuto', '自动化测试'),
               ('testTools', '测试工具'),
               ('testLife', '测试人生'),
               ('testPerformance', '性能测试'),
               ('testInterface', '接口测试'),
               ('testSecure', '安全测试')

        )

}

class Message():
    '''used to pop a window '''
    static = True
    style = 'btn-danger'
    header = 'Message'
    content = ''
    add_on = ''

    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)


ERROR = {
    "404": {
        "style": "btn-danger",
        "header": "404错误",
        "content": "懂不懂由你，反正我是懂了。",
        "add_on": ""
    },
    "duplicate": {
        "style": "btn-danger",
        "header": "重复错误",
        "content": "提交的信息存在重复，无法完成 !",
        "add_on": ""
    }
}

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage

def listing(request, page='', param=None, allObjects=None, pageNum=1):
    if pageNum < 1:
        pageNum = 1

    params = {}
    curPage = ''
    paginator = Paginator(allObjects, 20)

    # If page request (9999) is out of range, deliver last page of results.
    try:
        objects = paginator.page(pageNum)
    except (EmptyPage, InvalidPage):
        objects = paginator.page(paginator.num_pages)

    params['objects'] = objects
    if page: curPage = page
    if param: params.update(param)
    return render_to_response(curPage, params, context_instance=RequestContext(request))

