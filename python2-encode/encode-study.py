# coding=utf-8 将系统默认ASCII编码更改为utf-8

import sys
import chardet #检测字符编码

print chardet.detect('大鹏码字')
# 检测到当前的字符编码是 utf-8
# {'confidence': 0.938125, 'language': '', 'encoding': 'utf-8'}

print '大鹏码字' #输出乱码 utf-8--GB2312 转码失败

print '大鹏码字'.decode('utf-8') #输出正确 utf-8--unicode--GB2312转码成功