from coding_tree import AdaptiveCodingTree, AdaptiveNode
import copy
from string import ascii_lowercase

alpha = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}
e = 4
r = 11


def create_coding_trees(text):
    node_dict = {}
    node_list = []
    tree_list = []
    nyt_node = AdaptiveNode(0, 'NYT', None, 53)

    node_dict['NYT'] = nyt_node
    node_list.append(nyt_node)

    tree = AdaptiveCodingTree()
    tree.root = nyt_node

    tree_list.append(copy.deepcopy(tree))

    for sym in text:
        if sym not in node_dict:
            node_par = AdaptiveNode(1, None, None, nyt_node.weight)

            if nyt_node.parent is not None:
                node_par.parent = nyt_node.parent
                nyt_node.parent.l = node_par

            nyt_node.parent = node_par

            nyt_node.weight = node_par.weight - 2

            node_par.l = nyt_node
            node_par.r = AdaptiveNode(1, sym, node_par, node_par.weight - 1)
            node_dict[sym] = node_par.r

            node_list.append(node_par)
            node_list.append(node_par.r)

            if sym == text[0]:
                tree.root = node_par

        else:
            node = node_dict[sym]
            cur_node = node
            nodes = tree.level_order_exchange(len(node_list), cur_node)
            while cur_node != tree.get_root():
                for this_node in nodes:
                    if this_node.ord > cur_node.ord and this_node.value < cur_node.value:
                        exchange(this_node, cur_node)
                if cur_node.parent:
                    cur_node = cur_node.parent

            node.value += 1


        for node in reversed(node_list):

            if node.l is not None and node.r is not None:
                node.value = node.l.value + node.r.value
                if node.l.value > node.r.value:
                    left = node.l
                    node.l = node.r
                    node.r = left


        # APPEND THE TREE IN TREE_LIST
        tree_list.append(copy.deepcopy(tree))

    return tree_list, node_dict


def code_path(c_tree, sym):
    node = c_tree.get_node(sym)
    code = c_tree.code_by_path(node, '')

    return code


def exchange(node1, node2):
    if node1.parent and node1.parent.l == node1:
        node1.parent.l = node2
    elif node1.parent:
        node1.parent.r = node2
    if node2.parent and node2.parent.l == node2:
        node2.parent.l = node1
    elif node2.parent:
        node2.parent.r = node1

    if node1.parent and node2.parent:
        node1.parent, node2.parent = node2.parent, node1.parent
    node1.ord, node2.ord = node2.ord, node1.ord
    node1.value, node2.value = node2.value, node1.value
    if node1.symbol and node2.symbol:
        node2.symbol, node1.symbol = node1.symbol, node2.symbol


def fixed_code(sym):
    if sym == ' ':
        k = 27
    else:
        k = int(alpha[sym])

    if 1 <= k <= 2*r:
        fixed = bin(k - 1)[2:].zfill(e + 1)

    else:
        fixed = bin(k - r - 1)[2:].zfill(e)

    return fixed


def adaptive_huffman_encode(text, tree_list, full_node_dict):
    text = text.lower()
    final_code = ''
    node_dict = {}

    for i in range(len(text)):
        sym = text[i]
        if sym not in node_dict:
            node_dict[sym] = full_node_dict[sym]
            nyt_code = '' if i == 0 else code_path(tree_list[i], 'NYT')
            fixed = fixed_code(sym)
            code = nyt_code + fixed
            final_code += code
        else:
            code = code_path(tree_list[i], sym)
            final_code += code

    return final_code


def adaptive_huffman_decode(code, tree_list):
    text = ''
    i = 0
    tree = tree_list[0]
    j = 0
    current_node = tree.get_root()
    nyt_code = ''
    while j < len(code):
        bit = code[j]

        if bit == '0' and current_node.l:
            current_node = current_node.l
            nyt_code += '0'
        elif bit == '1' and current_node.r:
            current_node = current_node.r
            nyt_code += '1'
        if current_node.l is None and current_node.r is None:
            if current_node.symbol == 'NYT':
                l = 0 if j == 0 else 1
                fixed_bin = code[j+l:j+l+e]

                fixed = int(fixed_bin, 2)
                if fixed < r:
                    fixed_bin += code[j+l+e]
                    fixed = int(int(fixed_bin, 2)) + 1
                    letter = list(alpha.keys())[list(alpha.values()).index(str(fixed))]
                    text += letter
                    j = j + l + e + 1
                else:
                    fixed += r + 1
                    if fixed == 27:
                        text += ' '
                    else:
                        letter = list(alpha.keys())[list(alpha.values()).index(str(fixed))]
                        text += letter
                    j = j + l + e

            else:
                text += current_node.symbol
                j += 1

            i += 1
            tree = tree_list[i]
            current_node = tree.get_root()
            nyt_code = ''
        else:
            j += 1

    return text






