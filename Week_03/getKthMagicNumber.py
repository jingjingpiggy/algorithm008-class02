#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def getKthMagicNumber(k):
#    ans, a, b, c = [1], 0, 0, 0
#    for _ in range(k - 1):
#        ans.append(min(ans[a] * 3, ans[b] * 5, ans[c] * 7))
#        a += ans[-1] == ans[a] * 3
#        b += ans[-1] == ans[b] * 5
#        c += ans[-1] == ans[c] * 7
#    return ans[-1]
    res = [1] * k
    idx3, idx5, idx7 = 0, 0, 0   # 分别表示能被3 5 7整除的数的下表
    for i in range(1, k):
        res[i] = min(res[idx3]*3, res[idx5]*5, res[idx7]*7)  # 最小的填充到当前位置

        if res[i] == res[idx3]*3:   # 如果3的倍数最小，那么当前是能被3整除的数，更新idx3
            idx3 += 1
        if res[i] == res[idx5]*5:   # 如果5的倍数最小，那么当前是能被5整除的数
            idx5 += 1
        if res[i] == res[idx7]*7:
            idx7 += 1
    return res[k-1]


print(getKthMagicNumber(5))
