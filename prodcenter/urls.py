from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prodcenter.views.home', name='home'),
    # url(r'^prodcenter/', include('prodcenter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^ckeditor/', include('ckeditor.urls')),

    (r'^static/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'base/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^accounts/change_pwd/$', 'django.contrib.auth.views.password_change', {'template_name': 'base/index.html', 'post_change_redirect': '/',}),
)

urlpatterns += patterns('base.views',
    (r'^$', 'index'),
)

urlpatterns += patterns('product.products',
    (r'^product/home/$', 'home'),
    (r'^product/create/$', 'create'),
    (r'^product/(?P<id>\d*)/detail/$', 'detail'),
    (r'^product/(?P<id>\d*)/update/$', 'update'),
)

urlpatterns += patterns('product.functions',
    (r'^product/function/create/$', 'create'),
    (r'^product/function/(?P<id>\d*)/detail/$', 'detail'),
    (r'^product/function/(?P<id>\d*)/update/$', 'update'),
)

urlpatterns += patterns('product.versions',
    (r'^product/version/home/$', 'home'),
    (r'^product/(?P<prodId>\d+)/version/list$', 'list'),
    (r'^product/version/create/$', 'create'),
    (r'^product/version/(?P<id>\d*)/detail/$', 'detail'),
    (r'^product/version/(?P<id>\d*)/update/$', 'update'),
    (r'^product/version/map/$', 'versionMap'),
    (r'^product/version/search/$', 'versionSearch'),
    # (r'^product/version/(?P<id>\d*)/delete/$', 'delete'),
    #(r'^product/version/(?P<id>\d*)/download/$', 'download'),
)

urlpatterns += patterns('known.views',
    (r'^known/home/(?P<pageNum>\d*)$', 'home'),
    (r'^known/space/(?P<pageNum>\d*)$', 'space'),
    (r'^known/article/create/$', 'createArticle'),
    (r'^known/(?P<id>\d*)/detail/$', 'detailArticle'),
    (r'^known/(?P<id>\d+)/update/$', 'updateArticle'),
    (r'^known/folder/(?P<folder>\w+)/(?P<pageNum>\d*)$', 'listByFolder'),
    (r'^known/status/(?P<status>\d+)/(?P<pageNum>\d*)$', 'listByStatus'),
)