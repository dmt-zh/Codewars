# "recede"   =>  "()()()"
def duplicate_encode(word):
    from collections import Counter
    counter = Counter(word)
    return "".join(")" if counter[i] > 1 else "(" for i in word)

print(duplicate_encode('(( @'))