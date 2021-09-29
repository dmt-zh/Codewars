# Imagine the following situations:
# A truck loading cargo
# A shopper on a budget
# A thief stealing from a house using a large bag
# A child eating candy very quickly
# All of these are examples of The Knapsack Problem, where there are
# more things that you want to take with you than you can take with you.

# The Kata
# Write the function knapsack that takes two parameters, capacity and items, and returns
# a list of quantities. capacity will be a positive number items will be an array of arrays
# of positive numbers that gives the items' sizes and values in the form [[size 1, value 1],
# [size 2, value 2], ...] knapsack will return an array of integers that specifies the quantity
# of each item to take according to the greedy solution (the order of the quantities must match the order of items).

def knapsack(capacity, items):
    bag = {k[0]: 0 for k in items}
    acc = 0
    stuff = sorted(items, key=lambda x: x[1]/x[0])
    while acc < capacity:
        if len(stuff) == 0:
            break
        item = stuff.pop()
        while acc+item[0] <= capacity:
            bag[item[0]] = 1 + bag[item[0]]
            acc += item[0]
    return [i for i in bag.values()]
