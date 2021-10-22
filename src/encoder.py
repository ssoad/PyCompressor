from priority_queue import PriorityQueue

class Encoder:
    __statistics = {}
    __codes = {}

    def __init__(self):
        pass

    def encode(self, message):
        self.__create_statistics(message)
        tree_root = self.__create_huffman_tree()
        self.__generate_codes(tree_root, "")
        
        compressed_message = ""
        for sign in message:
            compressed_message = compressed_message + self.__codes[sign]

        return (
            compressed_message,
            self.__codes
        )

    def __create_statistics(self, message):
        self.__statistics.clear()

        for sign in message:
            if sign in self.__statistics.keys():
                self.__statistics[sign] = self.__statistics[sign] + 1
            else:
                self.__statistics[sign] = 1

    def __create_huffman_tree(self):
        priority_queue = PriorityQueue(lambda item1, item2: True if item1.frequency <= item2.frequency else False)

        # creating single-node-trees
        for key in self.__statistics.keys():
            node = TreeNode(key, self.__statistics[key], None, None)
            priority_queue.put(node)
        
        # building Huffman tree 
        while priority_queue.length() > 1:
            left_child = priority_queue.delete()
            right_child = priority_queue.delete()

            merged_node = TreeNode.merge(left_child, right_child)
            priority_queue.put(merged_node)
        
        return priority_queue.delete()

    def __generate_codes(self, node, code):
        if node is not None and node.sign is not None:
            self.__codes[node.sign] = code
        elif node is not None:
            if node.left_child is not None:
                new_code = code + '0'
                self.__generate_codes(node.left_child, new_code)
            if node.right_child is not None:
                new_code = code + '1'
                self.__generate_codes(node.right_child, new_code)

    #@deprecated
    def show_codes(self):
        for key in self.__codes.keys():
            print('{} -> {}'.format(key, self.__codes[key]))

    #@deprecated
    def show_tree(self, node, lvl):
        left_child_sign = node.left_child.frequency if node is not None and node.left_child is not None else None
        right_child_sign = node.right_child.frequency if node is not None and node.right_child is not None else None
        my_sign = node.frequency if node is not None else None

        print(lvl)
        print("left_child: " + str(left_child_sign) + " | me: " + str(my_sign) + " | right_child: " + str(right_child_sign))
    
        if node.left_child is not None :
            self.show_tree(node.left_child, lvl + 1)
        if node.right_child is not None:
            self.show_tree(node.right_child, lvl + 1)

class TreeNode:
    sign = None
    frequency = None
    left_child = None
    right_child = None

    def __init__(self, sign, frequency, left_child, right_child):
        self.sign = sign
        self.frequency = frequency
        self.left_child = left_child
        self.right_child = right_child

    @classmethod
    def merge(cls, left_child, right_child):
        calc_frequency = left_child.frequency if left_child.frequency is not None else 0
        calc_frequency = calc_frequency + right_child.frequency if right_child.frequency is not None else 0

        merged_node = TreeNode(None, calc_frequency, left_child, right_child)
        return merged_node

    def __lt__(self, other):
        return self.frequency < other.frequency
    
    def __le__(self, other):
        return self.frequency <= other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __ge__(self, other):
        return self.frequency >= other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency
    
    def __ne__(self, other):
        return self.frequency != other.frequency
