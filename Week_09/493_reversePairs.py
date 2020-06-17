#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
class Solution:
    def __init__(self):
        self.bit = []
        self.n = 0

    def query(self, i: int):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def update(self, i: int, x: int = 1):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def reversePairs(self, nums: List[int]) -> int:
        x = list(set(nums))
        nn, ind = sorted(list(set(x + list(map(lambda a: 2 * a, x))))), 1
        disc = {}
        for n in nn:
            disc[n] = ind
            ind += 1
        self.n, self.bit = ind, [0 for _ in range(ind + 5)]
        ret = 0
        for n in nums:
            if ind >= disc[n * 2]:
                ret += self.query(i=ind) - self.query(i=disc[n * 2])
            self.update(disc[n])
        return ret
