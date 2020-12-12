from coding_tree import AdaptiveCodingTree, AdaptiveNode
import copy
from string import ascii_lowercase

alpha = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}


def create_coding_trees(text):
    node_dict = {}
    node_list = []
    tree_list = []
    leaf_list = []
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

            # UPDATE NODE VALUES
            for node in reversed(node_list):
                if node.l is not None and node.r is not None:
                    node.value = node.l.value + node.r.value
                    if node.l.value > node.r.value:
                        left = node.l
                        node.l = node.r
                        node.r = left
                # print('SYM:', node.symbol, 'VAL:', node.value, 'WEIGHT:', node.weight)

        else:
            node = node_dict[sym]
            node.value += 1

            # UPDATE NODE VALUES
            for node in reversed(node_list):
                if node.l is not None and node.r is not None:
                    node.value = node.l.value + node.r.value
                    if node.l.value > node.r.value:
                        left = node.l
                        node.l = node.r
                        node.r = left
                # print('SYM:', node.symbol, 'VAL:', node.value, 'WEIGHT:', node.weight)

        # APPEND THE TREE IN TREE_LIST
        tree_list.append(copy.deepcopy(tree))

    return tree_list, node_dict


def code_path(c_tree, sym):
    node = c_tree.get_node(sym)
    code = c_tree.code_by_path(node, '')

    return code


def fixed_code(sym):
    e = 4
    r = 11
    if sym == ' ':
        k = 27
    else:
        k = int(alpha[sym])

    if 1 <= k <= 2*r:
        fixed = bin(k - 1)[2:].zfill(e + 1)

    else:
        fixed = bin(k - r - 1)[2:].zfill(e)

    return fixed


def adaptive_huffman_encode(text):
    final_code = ''
    node_dict = {}
    tree_list, full_node_dict = create_coding_trees(text)

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


def adaptive_huffman_decode(code):
    # TODO
    pass


def main():
    print(adaptive_huffman_encode('aardvark'))


main()
