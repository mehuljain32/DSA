import math
import sys
def ii():
  return int(input())

def li():
  return list(map(int,input().split()))

def si():
    return input()

def solve():
    n = ii()
    s = si()
    p = si()
    res = 999999

    vowel = ['a','i','e','o','u']
    cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    alpha = ['a','i','e','o','u', 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    # for i in range(len(p)):
    #     if p[i] == s[i]:
    #         continue
            
    #     elif (p[i] in vowel and s[i] in vowel) or (p[i] in cons and s[i] in cons):
    #         res += 2
        
    #     elif (p[i] in vowel and s[i] in cons) or (p[i] in cons and s[i] in vowel):
    #         res += 1
    #     else:
    #         res += 1
    
    if p == s:
        print(0)
        return

    if '?' in s or '?' in p:
        for i in alpha:
            ans = helper(p.replace('?', i), s.replace('?', i), vowel, cons)
            res = min(res, ans)
    else:
        res = helper(p,s,vowel, cons)
    print(res)
    return

    # abcde?
    # ehio??
    #2 + 2 + 1 + 1 +
  
def helper(p, s, vowel, cons):
    res = 0
    for i in range(len(p)):
        if p[i] == s[i]:
            continue
            
        elif (p[i] in vowel and s[i] in vowel) or (p[i] in cons and s[i] in cons):
            res += 2
        
        elif (p[i] in vowel and s[i] in cons) or (p[i] in cons and s[i] in vowel):
            res += 1
        else:
            res += 1
    return res
t = ii()
for _ in range(t):
  solve()