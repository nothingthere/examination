#!/usr/bin/python3
# notebook.py
# Author: Claudio <3261958605@qq.com>
# Created: 2017-08-15 22:04:20
# Code:
'''
notebook UI
'''

import choices_frame
import completions_frame
import judgments_frame
from tkinter import ttk


class Tabs(ttk.Notebook):
    def __init__(self, master):
        super(Tabs, self).__init__(master)
        self.choices_tab = choices_frame.Frame(self, 'choices.json')
        self.judgments_tab = judgments_frame.Frame(self, 'judgments.json')
        self.completions_tab = completions_frame.Frame(self,
                                                       'completions.json')
        self.tabs = [self.choices_tab,
                     self.judgments_tab, self.completions_tab]

        self.add_tabs()

        self.event_generate("<<NotebookTabChanged>>")
        self.bind("<<NotebookTabChanged>>", self.on_tab_change)

    def add_tabs(self):
        self.add(self.choices_tab, text='选择题')
        self.add(self.judgments_tab, text='判断题')
        self.add(self.completions_tab, text='填空题')

        for tab in self.tabs:
            tab.config(width=800, height=400)
            tab.grid_propagate(0)

    def on_tab_change(self, event):
        current_index = self.index(self.select())
        # print(current_index)
        # 为了给单独tab所在frame添加事件
        # 参考自：https://stackoverflow.com/questions/16923167/why-doesnt-the-bind-method-work-with-a-frame-widget-in-tkinter
        self.tabs[current_index].focus_set()
