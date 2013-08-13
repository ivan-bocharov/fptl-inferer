__author__ = 'ivan-bocharov'


class FPTLNode():
    pass


class ParallelNode(FPTLNode):

    def __init__(self, l_node=None, r_node=None):
        self.left_node = l_node
        self.right_node = r_node
    pass


class SequentialNode(FPTLNode):

    def __init__(self, f_node, s_node):
        self.first_node = f_node
        self.second_node = s_node


class ConditionalNode(FPTLNode):

    def __init__(self, c_node, t_node, f_node):
        self.condition_node = c_node
        self.true_branch = t_node
        self.false_branch = f_node



class FunctionalNode(FPTLNode):
    pass

