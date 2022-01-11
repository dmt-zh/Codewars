# Write a program that, given a word, computes the scrabble score for that word.

# Letter Values
# You'll need these:

# Letter                           Value
# A, E, I, O, U, L, N, R, S, T       1
# D, G                               2
# B, C, M, P                         3
# F, H, V, W, Y                      4
# K                                  5
# J, X                               8
# Q, Z                               10

# There will be a preloaded dictionary dict_scores with all these values: dict_scores["E"] == 1

# Examples

# "cabbage" should be scored as worth 14 points:
# 3 points for C
# 1 point for A, twice
# 3 points for B, twice
# 2 points for G
# 1 point for E

# And to total: 3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 14

from collections import Counter
def scrabble_score(st):
    if len(st) < 1:
        return 0
    else:
        d = Counter(st.upper())
        return sum([dict_scores[i] * j for i, j in d.items() if i.isalpha()])