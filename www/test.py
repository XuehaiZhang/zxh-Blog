#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'

# import asyncio
# from www import orm
# from www.models import User
# def test(loop):
#     yield from orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
#     u = User(name='Test6', email='test6@test.com', passwd='test', image='about:blank')
#     yield from u.save()
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.close()

import inspect


def fun(a, b, c=3, *, city='Beijing', **kw):
    pass

params = inspect.signature(fun).parameters
for name, param in params.items():
    print(name, param)
    print(param.kind)
    print(param.default)


def fun(a, b, c=3, *required, **re):
    pass

params = inspect.signature(fun).parameters
for name, param in params.items():
    print(name, param)
    print(param.kind)
    print(param.default)


# def fn(n):
#     if n == 1:
#         return True
#
# print(fn(1))
# print(fn(2))