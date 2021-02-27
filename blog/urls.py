from django.urls import path, include
# 应用级别路由配置

import blog.views

urlpatterns = [
    path('hello_world', blog.views.hello_world),
    path('content', blog.views.article_content),
    path('index', blog.views.get_index_page, name='index'),
    # path('detail', blog.views.get_detail_page),
    path("detail/<int:article_id>", blog.views.get_detail_page),
]