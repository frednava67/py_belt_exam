from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),    
    url(r'^quotes$', views.index), # or whatever is needed
    url(r'^logoff$', views.logoff),   
    url(r'^process_add$', views.process_add),        
    url(r'^process_delete$', views.process_delete),    
    url(r'^user/(?P<userid>[0-9]+)$', views.show_user),   
    url(r'^myaccount/(?P<userid>[0-9]+)$', views.edit_user),       
    url(r'^process_edit$', views.process_edit),     
    url(r'^process_like$', views.process_like),         
]