#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def ladderLength(beginWord, endWord, wordList):
    from collections import defaultdict
    from collections import deque

    if endWord not in wordList or not endWord or not beginWord or not wordList:return 0

    all_combo_dict = defaultdict(list)
    L = len(beginWord)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

    visited = set()
    queue = deque([(beginWord, 1)])

    while queue:
        #import ipdb;ipdb.set_trace()
        current, level = queue.popleft()
        if current not in visited:
            for i in range(L):
                inter = current[:i] + "*" + current[i+1:]
                for w in all_combo_dict[inter]:
                    if w == endWord:
                        return level +1
                    else:
                        visited.add(current)
                        queue.append((w, level+1))

    return 0

print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
