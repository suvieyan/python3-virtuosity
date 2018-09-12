"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
import re
# log是读取到的日志，可以为组命名
log = ''
re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2-\3-\1',log)