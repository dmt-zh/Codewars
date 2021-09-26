# For a given string s find the character c (or C) with longest consecutive repetition and return: (c, l)
# where l (or L) is the length of the repetition. If there are two or more characters with the same l return
# the first in order of appearance. For empty string return: ('', 0).

def longest_repetition(word):
    if len(word) < 1:
        return ('', 0)
    else:
        chars = []
        nums = []
        i = 0
        n = word[0]
        for c in word:
            if c == n:
                i += 1
            else:
                chars += n
                nums.append(i)
                n = c
                i = 1
        chars += n
        nums.append(i)
        return (chars[nums.index(max(nums))], max(nums))