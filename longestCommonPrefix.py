import os
def longestCommonPrefix(strs):
    
    #case, empty
    if not strs:
        return ""
    
    #get minimum prefix
    mini = min(strs)
    #get max prefix
    maxi = max(strs) 
    
    #case, no prefix
    if not mini:
        return "" 
    
    for i, val in enumerate(mini):
        if maxi[i] != mini[i]:
            return maxi[:i]
    return mini[:]

def longestAlternative(strs):
    #taken from leetcode, apparently already implemented solution available in python

    return os.path.commonprefix(strs)

print(longestAlternative(["apple", "apply", "apparently"]))
print(longestCommonPrefix(["apple", "apply", "apparently"]))

    