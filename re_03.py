# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 下午5:20
# @Author  : baby松
# @FileName: re_03.py
# @Software: PyCharm
"""
忽略大小写
"""
import re
mystring = "sfhSKFHSKFHdskfhskfhskfhksfs"
result = re.compile(r'h|s', re.S|re.IGNORECASE).findall(mystring)
print(result)

