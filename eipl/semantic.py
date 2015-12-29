__author__ = 'freddy'

scope_stack = []

def remove_scope():
    global scope_stack
    scope_stack.pop()

def add_scope(name):
    global scope_stack
    scope_stack.append(name)

def get_current_scope():
    global scope_stack
    return scope_stack[-1]

def init():
    global scope_stack
    scope_stack = []

