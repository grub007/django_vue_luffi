# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# Create your models here.

class Course(models.Model):
    title = models.CharField(verbose_name=u"课程名称", max_length=32)
    course_img = models.CharField(verbose_name=u"课程图片", max_length=64)
    level_choices = (
        (1, u'初级'),
        (2, u'中级'),
        (3, u'高级'),
    )
    level = models.IntegerField(choices=level_choices, default=1, verbose_name=u"课程等级")

    def __str__(self):
        return self.title

class CourseDetail(models.Model):
    """
    课程详细
    """
    course = models.OneToOneField(to="Course")
    why = models.CharField(max_length=255, verbose_name=u"为什么要学")
    slogon = models.CharField(verbose_name=u"口号", max_length=255)
    # 这边必须加related_name进行反向关联，因为CourseDetail中有两个关联字段，django无法判断具体用哪个字段进行反向关联
    recommend_courses = models.ManyToManyField(to="Course", verbose_name=u"推荐课程", related_name="rc")

    def __str__(self):
        return u"课程详细:{}".format(self.course.title)

class Chapter(models.Model):
    """
    章节
    """
    num = models.IntegerField(verbose_name=u"章节")
    name = models.CharField(verbose_name=u"章节名称", max_length=32)
    course = models.ForeignKey(verbose_name=u"所属课程", to="Course")

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    """
    用户登录表
    """
    user = models.CharField(max_length=32, null=True, verbose_name=u"用户名")
    pwd = models.CharField(max_length=64, null=True, verbose_name=u"密码")

    def __str__(self):
        return self.user

class UserToken(models.Model):
    """
    用户token表
    """
    token = models.CharField(max_length=64, null=True)
    user = models.OneToOneField(to=UserInfo, null=True)

    def __str__(self):
        return self.token
