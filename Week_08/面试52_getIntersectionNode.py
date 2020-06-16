#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def getIntersectionNode(headA, headB):
    node1, node2 = headA, headB

    while node1 != node2:
        node1 = node1.next if node1 else headB
        node2 = node2.next if node2 else headA

    return node1
