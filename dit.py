#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# class A(object):
#     def __init__(self):
#         self.n = 2
#
#     def add(self, m):
#         print('self is {0} @A.add'.format(self))
#         self.n += m
# class B(A):
#     def __init__(self):
#         self.n = 3
#
#     def add(self, m):
#         print('self is {0} @B.add'.format(self))
#         super(B, self).add(m)
#         self.n += 3
# class C(A):
#     def __init__(self):
#         self.n = 4
#
#     def add(self, m):
#         print('self is {0} @C.add'.format(self))
#         super(C, self).add(m)
#         self.n += 4
# class D(B, C):
#     def __init__(self):
#         self.n = 5
#
#     def add(self, m):
#         print('self is {0} @D.add'.format(self))
#         super(D, self).add(m)
#         self.n += 5
#
#     def __call__(self, *args, **kwargs):
#         print self.n

# class A(object):
#     def __init__(self, *args, **kwargs):
#         print "A", args[0]
#
# class B(A): pass
#
# class C(object):
#     def __init__(self, *args, **kwargs):
#         print "C", args[0]
#
# class D(C): pass
#
# class E(B, D):
#     def __init__(self, *args, **kwargs):
#         super(E, self).__init__(*args, **kwargs)
#         D.__init__(self, *args, **kwargs)
#
# a = E(1)

# class A(object):
#     def __init__(self):
#         print "enter A"
#         print "leave A"
# class B(object):
#     def __init__(self):
#         print "enter B"
#         print "leave B"
# class C(A):
#     def __init__(self):
#         print "enter C"
#         super(C, self).__init__()
#         print "leave C"
# class D(A):
#     def __init__(self):
#         print "enter D"
#         super(D, self).__init__()
#         print "leave D"
# class E(B, C):
#     def __init__(self):
#         print "enter E"
#         B.__init__(self)
#         C.__init__(self)
#         print "leave E"
# class F(E, D):
#     def __init__(self):
#         print "enter F"
#         E.__init__(self)
#         D.__init__(self)
#         print "leave F"
#
# f = F()

# import random, os
# import xlsxwriter
#
# def create_dgit(num):
#     count = 0
#     foo = [lambda x, y: x+y, lambda x, y: x-y]
#     while True:
#         if count == num:
#             break
#         a, b, c = random.randint(1, 20), random.randint(1, 20), random.randint(0, 1)
#         if foo[c](a, b) <= 20 and foo[c](a, b) > 0:
#             yield "{} + {} =".format(a, b) if c == 0 else "{} - {} =".format(a, b)
#             count += 1
#
# if __name__ == "__main__":
#     row, col = 0, 0
#     workbook = xlsxwriter.Workbook('exercises.xlsx')
#     worksheet = workbook.add_worksheet()
#
#     for i in create_dgit(1000):
#         if col > 4:
#             row += 1
#             col = 0
#         worksheet.write(row, col, i)
#         col += 1
#     workbook.close()

# class test(object):
#
#     __key = 123
#
#     def __init__(self, args):
#         self.a = 1
#         self.__key += args
#
#     def aaa(self):
#         return self.__key + 1
#
# c = test(1)
# print c.__dict__
# print test.__dict__
# print c.aaa()
# print c.__dict__
# print test.__dict__

# from abc import ABCMeta, abstractmethod
#
# class Person(object):
#
#     def __init__(self, name, args):
#         self.__name = name
#         self.__age = args
#
#     @property
#     def name(self):
#         return self.__name + "NB"
#
#     @name.setter
#     def name(self, newname):
#         """
#         实现私有属性的变更
#         :param newname:
#         :return:
#         """
#         self.__name = newname
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.deleter
#     def age(self):
#         """
#         实现属性方法的删除
#         :return:
#         """
#         del self.__age
#
# a = Person("阿三", 10)
# a.c = "aaa"
# print a.c
# del a.__dict__["c"]
# print a.__dict__

import urllib

HR_API_URL = "http://uuq.cnsuning.com/uum-unify-query-web/employeeInfo"
HR_API_USER = "ZAB"
HR_API_PASSWORD = "Zra1sm3[h[R3"


def testaa(jobid):
    params = urllib.urlencode({"clientKey": HR_API_PASSWORD, "clientId": HR_API_USER,
                               "employeeId": jobid})
    req = urllib.urlopen("{}?{}".format(HR_API_URL, params))
    print req.read()

if __name__ == "__main__":
    testaa('88417960')