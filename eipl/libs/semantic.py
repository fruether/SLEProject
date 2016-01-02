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

def init():
    global scope_stack
    scope_stack = []

def add_context(terminal, value):
    global node_context
    if terminal in node_context.keys():
        node_context[terminal] +=value
    else:
        node_context[terminal] = [value]

def terminal_list(terminal):
    global node_context
    return node_context[terminal] if terminal in node_context.keys() else []

def release_node():
    global node_context
    node_context = {}

def exec_block(terminal, prefix, value):
    variable = terminal + prefix
    add_context(terminal, value)
    leftSide = terminal_list(terminal)
    setattr(libs.variables, variable, leftSide)
    
    return value
