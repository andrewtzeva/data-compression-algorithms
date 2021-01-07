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
        self.ord = None

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return "Value : {}, Symbol: {}, Weight: {}, Order: {}".format(self.value, self.symbol, self.weight, self.ord)


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

            print(root.value, root.ord),

            self.print_inorder(root.r)

    def level_order_exchange(self, node_list_len, node):

        if self.root is None:
            return

        nodes = []
        queue = []

        queue.append(self.root)
        i = 0

        while len(queue) > 0:

            queue[0]

            queue[0].ord = node_list_len - i
            node = queue.pop(0)
            nodes.append(node)

            # Enqueue left child
            if node.r is not None:
                queue.append(node.r)

            # Enqueue right child
            if node.l is not None:
                queue.append(node.l)

            i += 1
        return nodes



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

    def update(self, this_node, node_list):

        node = this_node

        while node != self.root:
            print(node)
            for n in node_list:
                if n is not None and node is not None:
                    if node.value == n.value and n.ord > node.ord and n != self.root:
                        print(n, node)
                        node.l, n.l = n.l, node.l
                        node.r, n.r = n.r, node.r
                        node.parent, n.parent = n.parent, node.parent
                        node.ord, n.ord = n.ord, node.ord
                        node.value, n.value = n.value, node.value
                        node = n.parent
                        break
                    else:
                        print('ok')
                        node = node.parent
                else:
                    break
            break







