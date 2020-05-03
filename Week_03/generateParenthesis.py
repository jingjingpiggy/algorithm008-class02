#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
# step1, 打印出所有左括号和右括号, 如果有n=3 则说明有2*n个括号, 没有验证括号的合法性
def generatParenthsis(n):
    def _generate(level, max, s):
    #terminator
        if level >= max:
            return
        #process current logic: left, right
        s1 = s + "("
        print(s1)
        s2 = s +")"
        print(s2)

        #drilldown
        _generate(level +1, max, s1)
        _generate(level +1, max, s2)
        #reverse states

    _generate(0, 2*n,"")

#print(generatParenthsis(1))

#step2, 增加验证括号合法性, 在生成阶段, 相当于剪枝
# left：可以随时加，指标别超标
# right：左个数 > 右个数
def generatParenthsis1(n):
    def _generate(left, right, n, s):
    #terminator
        if left == n and right == n:
            # filter the invalid s out
            print(s)
        #process current logic: left, right

       #drilldown
        if left < n:
            _generate(left+1, right, n, s + "(")

        if left > right:
            _generate(left, right+1, n, s + ")")
        #reverse states

    _generate(0, 0, n,"")

print(generatParenthsis1(3))
