# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 下午5:59
# @Author  : baby松
# @FileName: re_04.py
# @Software: PyCharm
"""
反向引用
"""
import re
mystring = "123123ewew"
result = re.compile(r'(\d+).*?\1([a-z]+)').findall(mystring)

print(result)