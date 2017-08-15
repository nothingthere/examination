#!/usr/bin/python3
# choices_frame2.py
# Author: Claudio <3261958605@qq.com>
# Created: 2017-08-15 18:04:16
# Code:
'''
选择题UI
'''
import meta_frame
import tkinter as tk
from public import FONT


class Frame(meta_frame.Frame):
    def __init__(self, master, filename):
        super(Frame, self).__init__(master, filename)
        self.add_buttons(5)
        self.add_indicate(6)

    def init_interactive(self):
        self.choice_A = tk.StringVar()
        self.choice_B = tk.StringVar()
        self.choice_C = tk.StringVar()
        self.choice_D = tk.StringVar()

        self.choose_A = tk.IntVar()
        self.choose_B = tk.IntVar()
        self.choose_C = tk.IntVar()
        self.choose_D = tk.IntVar()

    def add_interactive(self):
        tk.Checkbutton(self,
                       textvariable=self.choice_A,
                       wraplength=600,
                       justify=tk.LEFT,
                       font=FONT,
                       variable=self.choose_A).grid(row=1,
                                                    column=0,
                                                    columnspan=4,
                                                    sticky='w',
                                                    padx=(10, 0),
                                                    pady=5,
                                                    )
        tk.Checkbutton(self,
                       textvariable=self.choice_B,
                       wraplength=600,
                       justify=tk.LEFT,
                       font=FONT,
                       variable=self.choose_B).grid(row=2,
                                                    column=0,
                                                    columnspan=4,
                                                    padx=(10, 0),
                                                    pady=5,
                                                    sticky='w')
        tk.Checkbutton(self,
                       textvariable=self.choice_C,
                       wraplength=600,
                       justify=tk.LEFT,
                       font=FONT,
                       variable=self.choose_C).grid(row=3,
                                                    column=0,
                                                    columnspan=4,
                                                    padx=(10, 0),
                                                    pady=5,
                                                    sticky='w')
        tk.Checkbutton(self,
                       textvariable=self.choice_D,
                       wraplength=600,
                       justify=tk.LEFT,
                       font=FONT,
                       variable=self.choose_D).grid(row=4,
                                                    column=0,
                                                    columnspan=4,
                                                    padx=(10, 0),
                                                    pady=(5, 20),
                                                    sticky='w')

    def reset_interactive(self, index=0):
        question = self.qs.get_question()
        selections = question.get('S')

        self.choice_A.set('A.' + selections[0])
        self.choice_B.set('B.' + selections[1])
        self.choice_C.set('C.' + selections[2])
        self.choice_D.set('D.' + selections[3])

        # 所有选项重置
        self.choose_A.set(0)
        self.choose_B.set(0)
        self.choose_C.set(0)
        self.choose_D.set(0)

    def key(self, event):
        super(Frame, self).key(event)

        char = event.char.lower()
        if char == 'a':
            self.toggle_choose(self.choose_A)

        if char == 'b':
            self.toggle_choose(self.choose_B)

        if char == 'c':
            self.toggle_choose(self.choose_C)

        if char == 'd':
            self.toggle_choose(self.choose_D)

    @staticmethod
    def toggle_choose(choose):
        if choose.get():
            choose.set(0)
        else:
            choose.set(1)

    def check(self):
        # print('A', type(self.choose_A.get()))
        # print('B', self.choose_B.get())
        # print('C', self.choose_C.get())
        # print('D', self.choose_D.get())
        # 获取正确答案
        correct_answer = self.qs.get_answer()
        if not isinstance(correct_answer, list):
            correct_answer = list(correct_answer)

        correct_answer = set(correct_answer)
        # 获取提供答案
        answer = []
        if self.choose_A.get():
            answer.append('A')
        if self.choose_B.get():
            answer.append('B')
        if self.choose_C.get():
            answer.append('C')
        if self.choose_D.get():
            answer.append('D')

        answer = set(answer)

        is_correct = (not correct_answer.difference(answer)) and\
                     (not answer.difference(correct_answer))

        # print(correct_answer, answer, is_correct)
        if is_correct:
            self.show_correct()
        else:
            self.show_incorrect()
