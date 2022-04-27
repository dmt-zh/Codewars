# Linked Lists - Length & Count

# Implement Length() to count the number of nodes in a linked list.
# length(null) => 0
# length(1 -> 2 -> 3 -> null) => 3

# Implement Count() to count the occurrences of an integer in a linked list.
# count(null, 1) => 0
# count(1 -> 2 -> 3 -> null, 1) => 1
# count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) => 4

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def length(node):
    if node is None:
        return 0
    else:
        return 1 + length(node.next)

def count(node, data):
    if data is None:
        return 0
    else:
        if node.data == data:
            return 1 + count(node.next, data)
        else:
            return count(node.next, data)