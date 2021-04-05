from static_huffman_coding import static_huffman_decode, static_huffman_encode, create_coding_tree
from adaptive_huffman_coding import adaptive_huffman_decode, adaptive_huffman_encode, create_coding_trees
from lz77 import lz77_encode, lz77_decode
from utils.letter_frequencies import final_example
import time
import gzip
import bitarray

ba = bitarray.bitarray()

ba.frombytes(final_example.encode('utf-8'))


def static_huffman_time():
    start_encode = time.time()
    code = static_huffman_encode(final_example)
    end_encode = time.time()
    c_tree = create_coding_tree(final_example)[0]
    start_decode = time.time()
    text = static_huffman_decode(code, c_tree)
    end_decode = time.time()
    ratio = len(code) / len(ba)
    return 'Static: Encode time: {}, Decode time: {}, Ratio: {}'.format(end_encode - start_encode, end_decode - start_decode, ratio)


def adaptive_huffman_time():
    tree_list, full_node_dict = create_coding_trees(final_example)
    start_encode = time.time()
    code = adaptive_huffman_encode(final_example, tree_list, full_node_dict)
    end_encode = time.time()
    start_decode = time.time()
    text = adaptive_huffman_decode(code, tree_list)
    end_decode = time.time()
    ratio = len(code) / len(ba)
    return 'Adaptive: Encode time: {}, Decode time: {}, Ratio: {}'.format(end_encode - start_encode, end_decode - start_decode, ratio)


def lz77_time():
    start_encode = time.time()
    code = lz77_encode(final_example)
    end_encode = time.time()
    start_decode = time.time()
    text = lz77_decode(code)
    end_decode = time.time()
    ratio = len(code) / len(ba)
    return 'LZ77: Encode time: {}, Decode time: {}, Ratio: {}'.format(end_encode - start_encode, end_decode - start_decode, ratio)


def zip_time():
    final_example_b = bytes(final_example, 'utf-8')
    start_encode = time.time()
    code = gzip.compress(final_example_b)
    end_encode = time.time()
    start_decode = time.time()
    text = gzip.decompress(code)
    end_decode = time.time()
    ratio = len(code) / len(ba)
    return 'ZIP: Encode time: {}, Decode time: {}, Ratio: {}'.format(end_encode - start_encode, end_decode - start_decode, ratio)


def main():
    print(static_huffman_time())
    #print(adaptive_huffman_time())
    print(lz77_time())
    print(zip_time())


main()
