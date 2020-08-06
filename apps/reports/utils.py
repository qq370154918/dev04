# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/8/5 21:31 
  @Auth : 可优
  @File : utils.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 创建一个生成器，获取文件流，每次获取的是文件字节数据


def get_file_content(filename, chunk_size=1024):
    with open(filename, encoding='utf-8') as file:
        while True:
            content = file.read(chunk_size)
            # 如果文件结尾，那么content为None
            if not content:
                break
            yield content
