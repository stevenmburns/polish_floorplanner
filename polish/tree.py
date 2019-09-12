
from . import Trans

class Tree:
    def __init__(self, l, r, op):
        self.l_tr = None
        self.r_tr = None
        self.l = l
        self.r = r
        self.op = op

    def __str__( self):
        return "(" + str(self.l) + self.op + str(self.r) + ")"


def build_tree( polish):
    stack = []
    for obj in polish:
        if obj in ["|","-"]:
            r = stack.pop()
            l = stack.pop()
            stack.append(Tree( l, r, obj))
        else:
            stack.append(obj)

    assert len(stack) == 1
    
    return stack[0]
