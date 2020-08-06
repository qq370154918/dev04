# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/7/1 20:14 
  @Auth : 可优
  @File : serializers.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from rest_framework import serializers
from rest_framework import validators

from .models import Envs
from utils import common


class EnvsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Envs
        exclude = ('update_time', )

        extra_kwargs = {
            'create_time': {
                # 'read_only': False,
                'read_only': True,
                'format': common.datetime_fmt(),
            },

        }


class EnvsNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        fields = ('id', 'name')
