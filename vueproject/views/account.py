#!/usr/bin/env python
# -*- coding:utf-8 -*-

import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from vueproject.models import *

class Login(APIView):

    def post(self, request, *args, **kwargs):
        """
        用户认证登录
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {
            "code": 1001
        }
        username = request.data.get("username")
        password = request.data.get("password")
        user = UserInfo.objects.filter(user=username, pwd=password).first()
        if not user:
            ret["error"] = "用户名或密码错误"
            return Response(ret)
        token = str(uuid.uuid4())
        UserToken.objects.update_or_create(user=user, defaults={"token": token})
        ret["code"] = 1000
        ret["token"] = token
        return Response(ret)