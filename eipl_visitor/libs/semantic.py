__author__ = 'freddy'

scope_stack = []
node_context = {}


import libs.variables

def remove_scope():
    global scope_stack
    scope_stack.pop()

def add_scope(name):
    global scope_stack
    scope_stack.append(name)

def get_current_scope():
    global scope_stack
    return scope_stack[-1]

def unwraplexims(lexims):
    result = []
    for lexim in lexims:
        result.append(lexim.getText())
    return result
