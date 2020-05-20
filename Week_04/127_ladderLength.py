#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
from collections import defaultdict
from collections import deque
# Reference https://leetcode.com/problems/word-ladder/discuss/346920/Python3-Breadth-first-search

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0
    L = len(beginWord)
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

    queue = deque([(beginWord, 1)])

    visited = set()
    while queue:
        current_word, level = queue.popleft()
        if current_word not in visited:
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level+1
                    else:
                        visited.add(current_word)
                        queue.append((word, level+1))
    return 0

print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
