# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from base.models import CommonInfo, Group
from utils.static import STATUS

class Product(CommonInfo):
    '''a information box named product'''
    fullname = models.CharField('全称', max_length=50, help_text='名称缩写的全称')
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='类别')

    def __unicode__(self):
        return "%s<%s>" % (self.alias, self.name)

    def get_absolute_url(self):
        return "/product/detail/%s" % self.id

    def save(self, *args, **kwargs):
        prods = Product.objects.all()
        sameId = [prod.id for prod in prods if self.name==prod.name]
        if self.id or not sameId:
            super(Product, self).save(*args, **kwargs)
            return True, self.id
        else:
            return False, sameId[0]

class ProductForm(forms.ModelForm):
    '''Create a new Product'''
    group = forms.ModelChoiceField(label='所属分类', queryset=Group.objects.filter(parent__name__iexact='PRODUCT'))
    class Meta:
        model = Product
        fields = ('name', 'alias', 'fullname', 'group', 'desc')



class Function(CommonInfo):
    '''functions of products'''
    product = models.ForeignKey(Product, verbose_name='所属产品')
    status = models.CharField('状态', blank=True, max_length=15)

    def __unicode__(self):
        return '[%s]%s' %(self.product.name, self.name)

    def save(self, *args, **kwargs):
        funcs = Function.objects.all()
        sameId = [func.id for func in funcs if func.__unicode__() == self.__unicode__()]

        if self.id or not sameId:
            super(Function, self).save(*args, **kwargs)
            return True, self.id
        else:
            return False, sameId[0]

class FunctionForm(forms.ModelForm):
    '''Function Form'''
    status = forms.ChoiceField(label='功能状态', widget=forms.Select, choices=STATUS['FUNCTION'])
    class Meta:
        model = Function
        fields = ('name', 'product', 'status', 'desc')




class Version(CommonInfo):
    '''versions of products'''
    product = models.ForeignKey(Product, verbose_name='所属产品')
    depend = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='依赖版本')

    def __unicode__(self):
        return "%s-%s" % (self.product.name, self.name)

    def get_absolute_url(self):
        return "/product/version/%s/detail/" % self.id

    def save(self, *args, **kwargs):
        vers = Version.objects.all()
        sameId = [ver.id for ver in vers if self.__unicode__()==ver.__unicode__()]
        if self.id or not sameId:
            super(Version, self).save(*args, **kwargs)
            return True, self.id
        else:
            return False, sameId[0]

class VersionForm(forms.ModelForm):
    '''Create a new Version'''
    name = forms.CharField(max_length=20, label='版本号', help_text='版本号(无需产品名) eg. 4.6.5-Beta2 ; 6.4.0-RC1')
    depend = forms.ModelChoiceField(label='依赖版本', queryset=Version.objects.filter(product__name__exact='MOC'))
    class Meta:
        model = Version
        fields = ('product', 'name', 'depend', 'desc')



class Patch(CommonInfo):
    '''a information box named patch'''
    product = models.ForeignKey(Product, verbose_name='所属产品')
    depend = models.ManyToManyField(Version, verbose_name='修复版本')
    problem = models.TextField('修复问题', help_text='该补丁修复的问题')
    method = models.TextField('修复方法', help_text='如何使用补丁')
    rollback = models.TextField('回滚方法', help_text='出现异常如何回滚到之前状态')
    remark = models.TextField('备注', blank=True)

    def __unicode__(self):
        return "EBF-%d%d-%3.3d" % (self.product.id, self.created.year % 100, int(self.name))

class PatchForm(forms.ModelForm):
    '''Create a new Patch'''
    class Meta:
        model = Patch




from django.contrib import admin

admin.site.register(Product)
admin.site.register(Function)
admin.site.register(Version)
admin.site.register(Patch)