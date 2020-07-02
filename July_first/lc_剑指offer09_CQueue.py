#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
class CQueue:
    def __init__(self):
        self.A = []
        self.B = []

    def appendTail(self, value):
        self.A.append(value)

    def deleteHead(self):
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()
