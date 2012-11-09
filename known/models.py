# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from django.contrib.auth.models import User
from known.utils import STATIC

from ckeditor.widgets import CKEditorWidget

class Article(models.Model):
    '''the article in the KnowledgeBase'''
    title = models.CharField('文章标题', max_length=100)
    content = models.TextField('内容', blank=True, null=True)
    status = models.CharField('状态', blank=True, max_length=10)
    author = models.ForeignKey(User, verbose_name='作者')
    folder = models.CharField('分类', max_length=20)
    count = models.BigIntegerField('查看次数')
    created = models.DateTimeField('创建日期', auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField('更新日期', auto_now=True, null=True)

    class Meta:
        app_label = 'known'
        ordering = ('-created',)

    def __unicode__(self):
        return "%s" % (self.title)

    def get_absolute_url(self):
        return "/known/%s/detail/" % self.id

    def getFolder(self):
        for folder in STATIC['FOLDER']:
            if self.folder == folder[0]:
                return folder[1]
        return "未分类"

    def getStatus(self):
        for status in STATIC['STATUS']:
            if self.status == status[0]:
                return status[1]
        return "草稿"


class ArticleForm(forms.ModelForm):
    status = forms.ChoiceField(label='状态', widget=forms.RadioSelect, choices=STATIC['STATUS'])
    folder = forms.ChoiceField(label='分类', widget=forms.Select, choices=STATIC['FOLDER'])
    content = forms.CharField(label='内容', widget=CKEditorWidget(config_name='article'))
    class Meta:
        model = Article
        fields = ('title', 'folder', 'content', 'status')

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['title'].widget.attrs['class'] = "span10"
        self.fields['folder'].widget.attrs['class'] = "span2"
        self.fields['content'].widget.attrs['class'] = "span12"
        self.fields['status'].widget.attrs['class'] = "span6"


from django.contrib import admin

admin.site.register(Article)