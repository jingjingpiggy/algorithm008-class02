#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
# 快慢指针
def hasCycle(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

# hash
def hasCycle_hash(head):
    dic = {}
    while head:
        if head in dic:
            return True
        dic[head] = 1
        head = head.next
    return False
