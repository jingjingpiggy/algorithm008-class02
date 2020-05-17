#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def detectCycle(head):
    slow = fast = head

    while True:
        if not (fast and fast.next): return
        fast = fast.next.next
        slow = slow.next
        if fast == slow: break

    fast = head
    while fast != slow:
        fast, slow = fast.next, slow.next
    return fast
