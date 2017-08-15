#!/usr/bin/python3
# completions_frame.py
# Author: Claudio <3261958605@qq.com>
# Created: 2017-08-13 20:30:50
# Code:
'''
填空题界面
'''

import meta_frame
import tkinter as tk
from public import FONT


class Frame(meta_frame.Frame):
    def __init__(self, master, filename):
        super(Frame, self).__init__(master, filename)
        self.add_buttons(2)
        self.add_indicate(3)

    def init_interactive(self):
        self.input = tk.StringVar()
        self.entry = tk.Entry(
            self,
            textvariable=self.input,
            font=(FONT['family'], FONT['size'] + 2),
            width=60,
        )

    def add_interactive(self):
        self.entry.grid(
            row=1,
            column=0,
            columnspan=4,
            padx=(10, 0),
            pady=(20, 20),
            sticky='w'
        )

        self.entry.focus()

        def submit(event):
            char = event.char
            if char == '\r':
                self.check()

        self.entry.bind('<Key>', submit)

    def reset_interactive(self, index=0):
        self.input.set('')

    def check(self):
        '多个空格时，默认输入使用空格隔开'
        correct_answer = self.qs.get_answer()
        if not isinstance(correct_answer, list):
            correct_answer = correct_answer.split()

        correct_answer = set(correct_answer)

        # 获取填写答案
        answer = self.input.get().strip().split()
        answer = set(answer)

        is_correct = (not correct_answer.difference(answer)) and\
                     (not answer.difference(correct_answer))

        # print(correct_answer, answer, is_correct)
        if is_correct:
            self.show_correct()
        else:
            self.show_incorrect()

    def hint(self):
        answer = self.qs.get_question().get('A')

        if isinstance(answer, list):
            answer = ' '.join(answer)

        self.indicate.set(answer)
