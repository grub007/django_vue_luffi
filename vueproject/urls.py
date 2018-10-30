#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from vueproject.views import course
from vueproject.views import account

urlpatterns = [
    url(r"^course/$", course.CourseView.as_view({"get": "list"})),
    url(r"^course/(?P<pk>\d+)$", course.CourseView.as_view({"get": "retrieve"})),
    url(r"^auth/$", account.Login.as_view())
]