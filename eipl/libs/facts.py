__author__ = 'freddy'
import itertools

facts = []

def create_fact(type, *args):
    if len(args) == 2:
        facts.extend( map(lambda x :  (type,) + x, create_cartesian_product(args[0], args[1]))  )
    elif len(args) > 2 :
        facts.extend( map(lambda x :  (type,) + x, create_cartesian_product(args[0], args[1], args[2:-1])))
    else:
        if not isinstance(list, args[0]):
            first = [args[0]]
        else:
            first = args[0]
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