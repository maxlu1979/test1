# coding:utf-8
"""
#File       :3-10enumerate函数.py
#Time       :2022/9/7    10:15
#Author     :Max
#email      :314136458@qq.com
#Description:
"""

names = ['张三', '李四', '王二']

for i in range(len(names)):
    print(i, names[i])

print('分割线'.center(100, '-'))

for index, name in enumerate(names):
    print(index, name)
