from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.home_page, name='HomePage'),
    url(r'^soon/$', views.soon_page, name='SoonPage'),
    url(r'catalog/$', views.product_list, name='Catalog'),
    url(r'lookbook/$', views.look_book_page, name='LookBook'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='ProductList'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='ProductDetail')

]
