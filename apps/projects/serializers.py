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

from .models import Projects
from interfaces.models import Interfaces
from interfaces.serializers import InterfacesModelSerializer
from utils import common
from debugtalks.models import DebugTalks


class InterfacesNamesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interfaces
        fields = ('id', 'name')


class ProjectsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        exclude = ('update_time', )

        extra_kwargs = {
            'create_time': {
                'read_only': True,
                'format': common.datetime_fmt(),
            },

        }

    def create(self, validated_data):
        # 在创建项目时，同时创建一个空的debugtalk.py文件
        project = super().create(validated_data)
        DebugTalks.objects.create(project=project)
        return project


class ProjectsNamesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ('id', 'name')


class InterfacesByProjectIdModelSerializer(serializers.ModelSerializer):
    interfaces = InterfacesNamesModelSerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = ('interfaces', )


class InterfacesByProjectIdModelSerializer1(serializers.ModelSerializer):
    # interfaces = InterfacesNamesModelSerializer(many=True, read_only=True)

    class Meta:
        model = Interfaces
        fields = ('id', 'name')
