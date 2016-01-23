__author__ = 'freddy'
import itertools
import sys

facts = []

def create_fact(type, *args):
    if len(args) == 2:
        facts.extend( map(lambda x :  (type,) + x, create_cartesian_product(args[0], args[1]))  )
    elif len(args) > 2 :
        facts.extend( map(lambda x :  (type,) + x, create_cartesian_product(args[0], args[1], args[2:-1])))
    else:
        if not isinstance(args[0], list):
            first = [args[0]]
        else:
            first = args[0]

        if len(first) >= 1 and isinstance(first[0], tuple):
            facts.extend([(type,) + x for x in first])
        else:
            facts.extend([(type, x) for x in first])


def create_cartesian_product(first, second, *args):
    if not isinstance(first, list):
        first = [first]
    if not isinstance(second, list):
        second = [second]
    other = []
    for arg in args:
        if not list(arg):
            arg = [arg]
        other.append(arg)
    return list(itertools.product(first, second, *other))

def show():
    for x in facts:
        print (x)

def if_not_empty(cond, block):
    if cond is not None and len(cond) >= 1:
        for b in block:
            create_fact(*b)

"""
Create a binary relation between each two succeeding elements of a list.
"""
def next(leftList, rightList):
    if not isinstance(leftList, list) or not isinstance(rightList, list):
        sys.stderr.write("Both should be lists")
    set = leftList + rightList
    result = zip(set, set[1:])
    return  list(result)

"""
First element of a list.
"""
def first(list):
    return list[0]

"""
Last element of a list.
"""
def last(list):
    return list[-1]
"""
The set of all elements of a list.
"""
def each(list):
    return list

"""
Create a binary relation of type (int, node) that relates each element
in a list to its index.
"""
def index(list):
    result = []
    count = 0
    for x in list:
        result.append((count, x))
        count += 1
    return result

