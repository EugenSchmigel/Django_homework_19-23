from django.urls import path


from blog.views import IndexView, BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView
from blog.apps import BlogConfig


app_name = BlogConfig.name


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='edit_blog'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),

]
