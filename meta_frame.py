#!/usr/bin/python3
# meta_frame.py
# Author: Claudio <3261958605@qq.com>
# Created: 2017-08-15 16:36:33
# Code:
'''
元UI
'''

import tkinter as tk
from public import FONT
from questions import Questions


class Frame(tk.Frame):
    def __init__(self, master, filename):
        super(Frame, self).__init__(master)

        self.qs = Questions(filename)

        # 初始化
        self.init_question()
        self.init_interactive()
        self.init_buttons()
        self.init_indicate()

        self.reset_question()

        # 添加部件
        self.add_question()
        self.add_interactive()
        # self.add_buttons()
        # self.add_indicate()

        # 添加键盘事件
        self.bind('<Key>', self.key)

    def init_question(self):
        '添加问题变量'
        self.Q = tk.StringVar()

    def add_question(self):
        '添加问题对应的widget.'
        tk.Label(self,
                 textvariable=self.Q,
                 font=(FONT['family'], FONT['size'] + 2),
                 wraplength=600,
                 justify=tk.LEFT,
                 anchor=tk.W,
                 ).grid(row=0,
                        column=0,
                        columnspan=4,
                        sticky='w',
                        padx=(20, 0),
                        pady=(10, 10),
                        )

    def init_interactive(self):
        '初始化交互部件变量，如选项（选择题），空格（填空题）'
        pass

    def add_interactive(self):
        '添加选项、空格对应的widget'
        pass

    def init_buttons(self):
        '初始化操作按钮部件'
        self.hint_button = tk.Button(self,
                                     text='提示（h）',
                                     command=self.hint,
                                     width=10,
                                     font=(FONT['family'], FONT['size'] - 2),
                                     )
        self.redo_button = tk.Button(self,
                                     text='重做（r）',
                                     command=self.redo,
                                     width=10,
                                     font=(FONT['family'], FONT['size'] - 2),
                                     )
        self.next_question_button = tk.Button(self,
                                              text='下一题（n）',
                                              command=self.next,
                                              width=10,
                                              font=(FONT['family'],
                                                    FONT['size'] - 2),
                                              )
        self.confirm_button = tk.Button(self,
                                        text='确定（Enter）',
                                        command=self.check,
                                        width=10,
                                        font=(FONT['family'],
                                              FONT['size'] - 2),
                                        )

    def add_buttons(self, row):
        '添加按钮部件'
        self.hint_button.grid(row=row,
                              column=0,
                              padx=(10, 0),
                              pady=(0, 0),
                              sticky='w',
                              )
        self.redo_button.grid(row=row,
                              column=1,
                              padx=(0, 0),
                              pady=(0, 0),
                              sticky='w',
                              )
        self.next_question_button.grid(row=row,
                                       column=2,
                                       padx=(0, 0),
                                       pady=(0, 0),
                                       sticky='w',
                                       )
        self.confirm_button.grid(row=row,
                                 column=3,
                                 padx=(0, 0),
                                 pady=(0, 0),
                                 sticky='w',
                                 )

    def init_indicate(self):
        '初始化正确/错误提示部件'
        self.indicate = tk.StringVar()

    def add_indicate(self, row):
        '添加正确/错误提示部件'
        tk.Label(self,
                 textvariable=self.indicate,
                 font=(FONT['family'], FONT['size'] + 1),
                 ).grid(row=row,
                        column=0,
                        columnspan=4,
                        sticky='w',
                        pady=(20, 20),
                        padx=(20, 0),
                        )

    def reset_question(self, index=0):
        '''初始化问题，即获取当前问题，并将问题和提示
        变量至于初始状态
        '''
        self.qs.index += index
        question = self.qs.get_question()
        self.Q.set('{}/{}.{}'.format(self.qs.index + 1,
                                     self.qs.total,
                                     question.get('Q')))
        self.reset_interactive(index)
        self.indicate.set('')

    def reset_interactive(self, index=0):
        '重置交互，如选择状态，填空'
        pass

    def key(self, event):
        '按键捕捉回调函数'
        char = event.char.lower()
        # print('!!!')
        if char == 'h':
            self.hint()
        if char == 'r':
            self.redo()
        if char == 'n':
            self.next()
        if char == '\r':
            self.check()

    #
    # 逻辑部分
    #

    def hint(self):
        self.indicate.set(self.qs.get_question().get('A'))
        # print(self.qs.get_question().get('A'))

    def redo(self):
        self.reset_question(0)

    def next(self):
        self.reset_question(1)

    def check(self):
        pass

    def show_correct(self):
        self.indicate.set("正确")

    def show_incorrect(self):
        self.indicate.set("错误")
