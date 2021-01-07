
from coding_tree import Node, StaticCodingTree
from letter_frequencies import freqs as frequencies


def code_path(c_tree, nodes_dict, sym):
    node = nodes_dict[sym]
    code = c_tree.code_by_path(node, '')

    return code


def codes(c_tree, nodes_dict):
    code_dict = {}
    for symbol in nodes_dict.keys():
        code_dict[symbol] = code_path(c_tree, nodes_dict, symbol)
    return code_dict


def create_coding_tree(text):
    freqs = frequencies

    node_list = []
    node_dict = {}

    for i in freqs:
        node = Node(freqs[i], i, None)
        node_list.append(node)
        node_dict[i] = node

    c_tree = StaticCodingTree()
    c_tree.built_tree(node_list)

    return c_tree, node_dict


def static_huffman_encode(text):
    text = ''.join(x for x in text if x.isalpha() or x.isspace()).upper()
    c_tree, node_dict = create_coding_tree(text)

    code_dict = codes(c_tree, node_dict)

    code = ''
    for char in text:
        code += code_dict[char]

    return code


def static_huffman_decode(code, c_tree):
    text = ''

    current_node = c_tree.get_root()

    for bit in code:
        if bit == '0':
            current_node = current_node.l
        else:
            current_node = current_node.r

        if current_node.l is None and current_node.r is None:
            text += current_node.symbol
            current_node = c_tree.get_root()

    return text



