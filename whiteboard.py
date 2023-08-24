
# Write a function that takes two arrays of strings as input, a1 and a2. The function should 
# return an array r that contains all of the strings in a1 that are substrings of strings in a2, 
# sorted in lexicographical order.

# Example 1:
# a1 = ["arp", "live", "strong"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# solution(a1,a2) -> returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

def solution(a1, a2):
    result = []
    joined_li = ''.join(a2) # O(1)
    for word in a1: # O(n)
        if word in joined_li: # O(1)
            if word in result:
                pass
            else:
                result.append(word)
    result.sort()
    return result

joined_li = '~'.join(a2)
...
if word in biga2 and word not in result:
    result.append(word)

    def solution(a1, a2):
    empty_lst = []
    for word in a1:
        if word in ''.join(a2):
            empty_lst.append(word)
    empty_lst.sort()
    for i in range(len(empty_lst)-1):
        if empty_lst[i] == empty_lst[i+1]:
            empty_lst.remove(empty_lst[i])
    return empty_lst