# Given a string of words, you need to find the highest scoring word. Each letter of a word scores
# points according to its position in the alphabet: a = 1, b = 2, c = 3 etc. You need to return the
# highest scoring word as a string. If two words score the same, return the word that appears earliest
# in the original string. All letters will be lowercase and all inputs will be valid.


def high(x):
    import string

    weight = {
        x: y for x, y in zip(
        [str(char) for char in string.ascii_lowercase],
        [num for num in range(1, len(string.ascii_lowercase)+1)])
    }

    res = []
    sum = 0

    for i in x:
        for j in i:
            if j in weight:
                sum += weight[j]
            else:
                res.append(sum)
                sum = 0
    res.append(sum)
    return x.split()[res.index(max(res))]