from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'public.views.home', name='home'),
    url(r'^people/$', 'public.views.people', name='people'),
    url(r'^products/$', 'public.views.products', name='products'),
    url(r'^products/arduino-lcd-breadboard-box$', 'public.views.lcd_box', name='lcd_box'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
