import headpq


class Node:
    def __init__(self, val, sym, par):
        self.l = None
        self.r = None
        self.value = val
        self.symbol = sym
        self.parent = par

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return "Value : {}, Symbol: {}".format(self.value, self.symbol)


class AdaptiveNode:
    def __init__(self, val, sym, par, wt):
        self.l = None
        self.r = None
        self.value = val
        self.symbol = sym
        self.parent = par
        self.weight = wt

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return "Value : {}, Symbol: {}, Weight: {}".format(self.value, self.symbol, self.weight)


class StaticCodingTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def built_tree(self, node_list):
        headpq.heapify(node_list)
        while True:
            if len(node_list) == 1:
                self.root = node_list[0]
                break

            node1 = headpq.heappop(node_list)
            node2 = headpq.heappop(node_list)

            parent = Node(node1.value + node2.value, None, None)
            parent.l = node1
            node1.parent = parent
            parent.r = node2
            node2.parent = parent

            headpq.heappush(node_list, parent)

    def code_by_path(self, node, code):
        if node == self.root:
            return code[::-1]

        parent = node.parent

        if parent.l == node:
            code += '0'
        else:
            code += '1'

        return self.code_by_path(parent, code)


class AdaptiveCodingTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def print_inorder(self, root):
        if root:
            self.print_inorder(root.l)

            print(root.value),

            self.print_inorder(root.r)

    def code_by_path(self, node, code):
        if node == self.root:
            return code[::-1]

        parent = node.parent

        if parent.l == node:
            code += '0'
        else:
            code += '1'

        return self.code_by_path(parent, code)

    def get_node(self, sym):
        leaf = []
        self.find_node(sym, self.root, leaf)
        return leaf[0]

    def find_node(self, sym, root, leaf):
        if root is not None:
            if root.symbol == sym:
                leaf.append(root)
            for n in [root.l, root.r]:
                self.find_node(sym, n, leaf)





