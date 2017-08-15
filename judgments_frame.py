#!/usr/bin/python3
# judgment_frame.py
# Author: Claudio <3261958605@qq.com>
# Created: 2017-08-12 23:57:30
# Code:
'''
判断题UI
'''

import meta_frame
import tkinter as tk
from public import FONT


class Frame(meta_frame.Frame):
    def __init__(self, master, filename):
        super(Frame, self).__init__(master, filename)
        self.add_buttons(3)
        self.add_indicate(4)

    def init_interactive(self):
        self.judge = tk.BooleanVar()
        self.judge.set(True)

        self.yes_button = tk.Radiobutton(
            self,
            variable=self.judge,
            value=True,
            text='是',
            font=FONT,

        )
        self.no_button = tk.Radiobutton(
            self,
            variable=self.judge,
            value=False,
            text='否',
            font=FONT,
        )

    def add_interactive(self):
        self.yes_button.grid(
            row=1,
            column=0,
            columnspan=4,
            padx=(20, 0),
            pady=(10, 0),
            sticky='w'
        )

        self.no_button.grid(
            row=2,
            column=0,
            columnspan=4,
            padx=(20, 0),
            pady=(10, 30),
            sticky='w'
        )

    def reset_interactive(self, index=0):
        self.judge.set(True)

    def key(self, event):
        super(Frame, self).key(event)
        char = event.char.lower()
        # print(char)
        if char == '1':
            self.judge.set(True)
        if char == '0':
            self.judge.set(False)

    def check(self):
        correct_answer = self.qs.get_answer()
        answer = self.judge.get()

        is_correct = (correct_answer == answer)
        # print('正确答案', correct_answer)
        # print('我的答案', answer)
        # print('是否正确', is_correct)

        if is_correct:
            self.show_correct()
        else:
            self.show_incorrect()

    def hint(self):
        answer = self.qs.get_question().get('A')
        if answer:
            self.indicate.set('是')
        else:
            self.indicate.set('否')
