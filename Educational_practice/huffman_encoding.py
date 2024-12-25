import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0], frequency

def build_codes(node, current_code="", codes={}):
    if node is not None:
        if node.char is not None:
            codes[node.char] = current_code
        build_codes(node.left, current_code + "0", codes)
        build_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encode(text):
    root, frequency = build_huffman_tree(text)
    codes = build_codes(root)

    encoded_string = ''.join(codes[char] for char in text)
    unique_char_count = len(codes)
    encoded_size = len(encoded_string)

    print(f"{unique_char_count} {encoded_size}")
    for char, code in sorted(codes.items()):
        print(f"'{char}': {code}")
    print(encoded_string)

if __name__ == "__main__":
    input_string = "Errare humanum est."
    huffman_encode(input_string)
