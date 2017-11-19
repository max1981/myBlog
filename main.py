#coding:utf8
from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["python", "manage.py", "runnserver",'0.0.0.0:9998'])