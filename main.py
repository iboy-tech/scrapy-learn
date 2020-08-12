# -*- coding:UTF-8 -*-
#!/usr/bin/python
"""
@File    : main.py.py
@Time    : 2020/8/12 15:26
@Author  : iBoy
@Email   : iboy@iboy.tech
@Description : 
@Software: PyCharm
"""
from scrapy.cmdline import execute

import sys
import os

# 设置工程的目录，可以在任何路径下运行execute
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(["scrapy", "crawl", "jwc"])