# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from tagging.fields import TagField


class CommonInfo(models.Model):
    '''a abstract model : common information box'''
    name = models.CharField('名称', max_length=50)
    alias = models.CharField('别名', blank=True, max_length=80, help_text='中文名称')
    desc = models.TextField('描述', blank=True)
    created = models.DateTimeField('创建日期', blank=True, null=True)
    updated = models.DateTimeField('更新日期', auto_now=True, null=True)
    tags = TagField('标签', null=True, blank=True, max_length=500)

    class Meta:
        app_label = 'core'
        abstract = True
        ordering = ('-created',)

class Group(CommonInfo):
    '''used to group the information box'''
    parent = models.ForeignKey('self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='上级分类',
        related_name="parent_group_set")

    def __unicode__(self):
        return "%s-%s" % (self.parent.__unicode__() if self.parent else "Base", self.name)


class CommonInfoForm(models.Model):
    '''a abstract model : common form box'''
    #the value of type must equal with the lowercase name of subclass of this class
    group = models.ForeignKey(Group, verbose_name='表单类型') #used for internal relationship
    author = models.ForeignKey(User, verbose_name='提交人')
    created = models.DateTimeField('创建日期', auto_now_add=True, null=True)
    remark = models.TextField('备注', blank=True)

    class Meta:
        app_label = 'core'
        abstract = True
        ordering = ('-created',)


class Environment(models.Model):
    '''about environment'''
    server_os = models.CharField('服务器端操作系统', blank=True, max_length=15)
    server_chr = models.CharField('服务器端系统字符集', blank=True, max_length=10)
    dbms = models.CharField('数据库类型及版本', blank=True, max_length=20)
    db_chr = models.CharField('数据库字符集', blank=True, max_length=10)
    jre = models.CharField('java运行环境', blank=True, max_length=10)
    client_os = models.CharField('客户端操作系统', blank=True, max_length=15)
    browser = models.CharField('浏览器类型及版本', blank=True, max_length=10)
    addition = models.TextField('环境附加说明', blank=True, default='')

    class Meta:
        app_label = 'core'

    def __unicode__(self):
        return '%s-%s-%s-%s-%s-%s-%s' % (self.server_os,
                                         self.server_chr,
                                         self.dbms,
                                         self.db_chr,
                                         self.jre,
                                         self.client_os,
                                         self.browser
            )

    def save(self, *args, **kwargs):
        envs = Environment.objects.all()
        sameId = [env.id for env in envs if env.__unicode__() == self.__unicode__()]
        if self.id or not sameId:
            super(Environment, self).save(*args, **kwargs)
            return True, self.id
        else:
            return False, sameId[0]




from django.contrib import admin

admin.site.register(Group)
admin.site.register(Environment)