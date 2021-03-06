from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name='post'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.post_detail, name="post_detail"),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('FindJob', views.FindJob, name='FindJob'),
    path('createPost',views.createPost, name='createPost'),
    path('update_post/<str:pk>/', views.updatePost, name="update_post"),
    path('delete_post/<str:pk>/', views.deletePost, name="delete_post"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

