#!/usr/bin/python3
# meta.py
# Author: Claudio <3261958605@qq.com>
# Created: 2017-08-13 12:12:19
# Code:
'''
各个题型公用类

依赖：
json文件名：选择题choices.json、填空题completions.json、判断题judgments.json
'''

import json
import os.path


class Questions:
    def __init__(self, filename):

        # # 题型：选择题、判断题、填空题？
        # self.is_choices = False
        # self.is_completions = False
        # self.is_judgments = False
        self.questions = self.load(filename)
        # # print(self.questions)

        self.total = len(self.questions)    # 总题数
        self.index = 0                      # 当前第几题
        self.answered = 0                   # 已做个数
        self.incorrects = []                # 做错的题

    def load(self, filename):
        "加载json文件，返回python对象。"
        # 确定题型
        basename = os.path.basename(filename)
        if "choices.json" == basename:
            self.is_choices = True
        if "completions.json" == basename:
            self.is_completions = True
        if "judgments.json" == basename:
            self.is_judgments = True

        with open(filename, 'r') as fp:
            return json.load(fp)

    def get_question(self, index=0):
        "获取当前问题。"
        idx = self.index + index
        if idx >= self.total:
            idx = self.index = 0

        return self.questions[idx]

    def get_answer(self):
        "获取当前问题正确答案。"
        return self.get_question().get("A")

    # def check(self, answer):
    #     "检查答案。"
    #     correct_answer = self.get_answer()
    #     result = True

    #     if isinstance(correct_answer, list):
    #         if set(correct_answer).difference(set(answer)):
    #             result = False
    #     else:
    #         result = (correct_answer == answer)

    #     if not result:
    #         self.incorrects.append(self.index)

    #     return result

    # def report(self):
    #     "报告做题结果。"
    #     pass


if __name__ == '__main__':
    questions = Questions('choices.json')
    print(questions)
