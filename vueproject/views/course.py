#!/usr/bin/env python
# -*- coding: GBK-*- #

from rest_framework.views import APIView
from rest_framework.response import Response
from vueproject.serializers import *
from vueproject.models import *
from rest_framework.viewsets import GenericViewSet



class CourseView(GenericViewSet):

    authentication_classes = [MyAuth]

    def list(self, request, *args, **kwargs):
        '''
        获取全部课程
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = {"code": 1000, "data": None}

        try:
            queryset = Course.objects.all()
            ser = CourseSerializer(instance=queryset, many=True)
            ret["data"] = ser.data
        except Exception as e:
            ret["code"] = 1001
            ret["error"] = e
            ret["msg"] = u"课程获取失败"

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        '''
        获取课程详情
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = {"code": 1000, "data": None}

        try:
            queryset = CourseDetail.objects.filter(course_id=kwargs.get("pk")).first()
            if queryset:
                ser = CourseDetailSerializer(instance=queryset, many=False)
                ret["data"] = ser.data
            else:
                ret["data"] = None
        except Exception as e:
            ret["code"] = 1001
            ret["error"] = e
            ret["msg"] = u"课程详细获取失败"

        return Response(ret)