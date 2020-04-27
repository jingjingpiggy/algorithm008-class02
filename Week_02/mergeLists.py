#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def mergeKLists():
    # 暴力
    nodes = []
    head = point = ListNode(0)
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next
    for x in sorted(nodes):
        point.next = ListNode(x)
        point = point.next
    return point

    # heapq模块进行堆排序
    def mergeKLists(self, lists):
    import heapq
    head = point = ListNode(0)
    heap = []
    for l in lists:
        while l:
            heapq.heappush(heap, l.val)
            l = l.next
    while heap:
        val = heappop(heap)
        point.next = ListNode(val)
        point = point.next
    point.next = None
    return head.next
