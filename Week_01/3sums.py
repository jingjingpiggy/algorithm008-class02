#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authoir: Li jinjing <lijinjing@gmail.com>
# 暴力求解：时间复杂度O(n^3)
def threeSum(nums):
    res = []
    if len(nums) < 3:
        return []
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for x in range(j+1, len(nums)):
                if nums[x] + nums[i] + nums[j] == 0:
                    l = sorted([nums[x], nums[i], nums[j]])
                    if l not in res:
                        res.append(l)
    return res

# Hash: 时间复杂度O(n^2) a+b = -c, 有待debug
def threeSum_Hash(nums):
    if len(nums) < 3:
        return []
    '''先对数组排序, 遍历数组遇到与前一个元素相同的情况可直接跳过'''
    nums.sort()
    target_hash = {-x: i for i, x in enumerate(nums)}
    res = []
    res_hash = {}
    for i, first in enumerate(nums):
        '''当前元素与前一个元素相同时, 可直接跳过以优化性能'''
        if i > 0 and first == nums[i - 1]:
            continue
        for j, second in enumerate(nums[i + 1:]):
            '''检查两数之和是否存在于哈希表中'''
            if first + second in target_hash:
                target_index = target_hash[first + second]
                if target_index == i or target_index == i + j + 1:
                    continue
                '''将找到的结果存入另一个哈希表中, 避免包含重复结果'''
                row = sorted([first, second, nums[target_index]])
                key = ",".join([str(x) for x in row])
                if key not in res_hash:
                    res.append(row)
                    res_hash[key] = True
    return res

def threeSum_doublePointer(nums):
    nums.sort()
    res = []
    for k in range(len(nums)-2):
        if k > 0 and nums[k] == nums[k-1]:
            continue
        i, j = k + 1, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j] + nums[k]
            if s < 0:
                i += 1
            elif s > 0:
                j -= 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                print(res)
                while i < j and nums[i] == nums[i+1]:
                    i += 1
                while i < j and nums[j] == nums[j-1]:
                    j -= 1
                i += 1
                j -= 1
    return res

print(threeSum_doublePointer([-1, 0, 1, 2, -1, -4]))
