# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 下午3:45
# @Author  : baby松
# @FileName: re_01.py
# @Software: PyCharm
"""
排除型字符组
"""
import re
# 要求排除掉q后面带u的字符串
str_list = ['qufdfd', 'dfsaffqdfd', 'qdsfsq', 'sfsqu', 'sfqfsfs']
for str in str_list:
    result = re.compile(r'^.*?q[^u].*', re.S).findall(str)
    print(result)
