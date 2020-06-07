#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def containsDuplicate(nums):
    return False if len(set(nums)) == len(nums) else True
