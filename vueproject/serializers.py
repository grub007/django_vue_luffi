#!/usr/bin/env python
# -*- coding:utf-8 -*-

from rest_framework import serializers
from models import *
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from models import UserToken

class CourseSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source="get_level_display")

    class Meta:
        model = Course
        fields = ["id", "title", "course_img", "level"]

class CourseDetailSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="course.title")
    img = serializers.CharField(source="course.course_img")
    level = serializers.CharField(source="course.get_level_display")
    recommend_courses = serializers.SerializerMethodField()
    chapter = serializers.SerializerMethodField()

    class Meta:
        model = CourseDetail
        fields = ["course", "title", "slogon", "why", "img", "level", "recommend_courses", "chapter"]

    def get_recommend_courses(self, obj):
        #获取manytomany表的数据可以通过all()来获取所有映射的数据
        return [{"id": row.id, "title": row.title} for row in obj.recommend_courses.all()]

    def get_chapter(self, obj):
        #obj.course指向课程表，通过课程表反向查找章节通过章节表名（此时表名必须是小写）加set实现(chapter_set)通过.all
        # 获取所有章节
        queryset = obj.course.chapter_set.all()
        return [{"id": row.id, "name": row.name, "num": row.num} for row in queryset]


class MyAuth(BaseAuthentication):

    def authenticate(self, request):
        """
        判断请求头是否携带了token
        :param request:
        :return:
        """
        token = request.META.get("HTTP_TOKEN", None)
        obj = UserToken.objects.filter(token=token).first()
        if not obj:
            raise exceptions.AuthenticationFailed({"code": 1001, "error": "auth error"})
        return (obj.user.user, obj)