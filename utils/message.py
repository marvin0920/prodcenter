# -*- coding: utf-8 -*-

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
