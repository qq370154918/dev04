# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/6/15 21:54
  @Auth : 可优
  @File : urls.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from rest_framework.routers import SimpleRouter

from . import views


# 定义路由对象
router = SimpleRouter()
router.register(r'interfaces', views.InterfacesViewSet)

urlpatterns = [

]
urlpatterns += router.urls
