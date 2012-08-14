from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'public.views.home', name='home'),
    url(r'^about/$', 'public.views.people', name='about'),
    url(r'^contact/$', 'public.views.people', name='contact'),
    url(r'^people/$', 'public.views.people', name='people'),
    url(r'^products/$', 'public.views.products', name='products'),
    url(r'^products/baby-books$', 'public.views.products', name='baby_books'),
    url(r'^products/accounting$', 'public.views.products', name='accounting'),
    url(r'^products/arduino-lcd-breadboard-box$', 'public.views.lcd_box', name='lcd_box'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
	(r'^google2692f5ed78e5fbf4.html$', 'direct_to_template', {'template': 'google2692f5ed78e5fbf4.html'}),
)
