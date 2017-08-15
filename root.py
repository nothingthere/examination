#!/usr/bin/python3
# root.py
# Author: Claudio <3261958605@qq.com>
# Created: 2017-08-13 20:16:18
# Code:
'''
图形界面主窗口
'''


import notebook
import tkinter as tk

root = tk.Tk()

#
# 初始化窗口
#
root.title('题库练习demo')
root.geometry('+10+10')
root.resizable(False, False)
root.geometry('800x400')

#
# 添加组件
#

nb = notebook.Tabs(root)
nb.grid(row=0, column=0)

#
# 运行
#


root.mainloop()
