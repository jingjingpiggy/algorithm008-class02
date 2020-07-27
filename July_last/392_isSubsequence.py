class Solution:
    # double pointers, Om+n, O1 
    def isSubsequence(self, s, t):
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == n



def isSubsequence(s, t):
    import ipdb;ipdb.set_trace()
    n, m = len(s), len(t)

    f = [[0]*26 for _ in range(m)]
    f.append([m]*26)

    for i in range(m-1, -1, -1):
        for j in range(26):
            f[i][j] = i if ord(t[i]) == j + ord('a') else f[i+1][j]


    add = 0
    for i in range(n):
        if f[add][ord(s[i])-ord('a')] == m:
            return False
        add = f[add][ord(s[i])-ord('a')] + 1

    return True 

print(isSubsequence("abc", "ahbgdc"))
