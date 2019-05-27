# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 下午4:23
# @Author  : baby松
# @FileName: re_02.py
# @Software: PyCharm
import re
str_list = ['03/19/76', '03-19-76', '03.19.76']
for str in str_list:
    result = re.compile(r'[0-9]{2}[-./][0-9]{2}[-./][0-9]{2}', re.S).findall(str)
    print(result)