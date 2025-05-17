#5.11
#模块 一个包含 Python 代码的文件，通常以 .py 结尾 代码可以重复使用
"""
模块可以分为以下几类：

自定义模块：用户自己编写的模块。
标准库模块：Python 自带的模块，如 math、os、sys 等。
第三方模块：由其他开发者编写的模块，通常可以通过 pip 安装
"""

#自定义模块
"""
import  my_modules  #导入自定义模块
import os,sys,re #批量导入
# 通过 from 导入模块
# from filename import function  可读性较差不推荐
"""

"""
python 全局变量 __name__，用来控制 .py 文件在不同的应用场景下执行不同的逻辑

当文件被当做脚本执行时：__name__ 等于'__main__'
当文件被当做模块导入时：__name__等于模块名
"""

#模块的搜索路径
"""
1.当前目录：Python 首先在当前目录下查找要导入的模块
2.PYTHONPATH 环境变量：包含一系列目录名
3.标准库目录：Python 安装时自带的标准库所在的目录
4.site-packages 目录：第三方模块安装的默认位置
"""


#包是一个包含 __init__.py 文件的目录，它用于组织和管理相关的Python模块。

#当文件作为脚本执行的时候 __nama__ = __main__
#当文件作为模块导入的时候 __nama__ = 模块名

#使用 from 导入包  需要注意的是 from 后 import 导入的模块，必须是明确的一个不能带点
"""
from glance.db import models
"""
#import 导入包
"""
import glance.db.models

glance.db.models.register_models('mysql')
"""