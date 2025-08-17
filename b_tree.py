
from nodo import BNode

class BTree:
    def __init__(self, order):
        self.order = order
        self.root = BNode(order)

    def insert(self, key):
        root_node = self.root
        max_keys = self.order - 1
        if len(root_node.keys) == max_keys:
            new_root = BNode(self.order)
            new_root.leaf = False
            new_root.children.append(self.root)
            self.split(new_root, 0)
            self.insert_in_node(new_root, key)
            self.root = new_root
        else:
            self.insert_in_node(root_node, key)

    def insert_in_node(self, current_node, key):
        if current_node.leaf:
            current_node.keys.append(key)
            current_node.keys.sort()
        else:
            i = 0
            while i < len(current_node.keys) and key > current_node.keys[i]:
                i += 1
            if len(current_node.children[i].keys) == self.order - 1:
                self.split(current_node, i)
                # If the key is greater than the new key inserted in the current node, move the index forward
                if key > current_node.keys[i]:
                    i += 1
            self.insert_in_node(current_node.children[i], key)

    def split(self, parent_node, i):
        order = self.order
        child_node = parent_node.children[i]
        new_node = BNode(order)
        new_node.leaf = child_node.leaf

        # Traditional split: max keys = order-1, middle = (order-1)//2
        middle = (order - 1) // 2
        middle_key = child_node.keys[middle]
        # The new node receives the keys to the right of the middle
        new_node.keys = child_node.keys[middle + 1:]
        # The original child keeps the keys to the left of the middle
        child_node.keys = child_node.keys[:middle]

        if not child_node.leaf:
            new_node.children = child_node.children[middle + 1:]
            child_node.children = child_node.children[:middle + 1]

        parent_node.keys.insert(i, middle_key)
        parent_node.children.insert(i + 1, new_node)

    def display(self, current_node=None, level=0):
        if current_node is None:
            current_node = self.root
        if current_node.keys:
            print("Level", level, ":", current_node.keys)
        for child in current_node.children:
            if child.keys or not child.leaf:
                self.display(child, level + 1)

    def search(self, key, current_node=None):
        if current_node is None:
            current_node = self.root
        i = 0
        while i < len(current_node.keys) and key > current_node.keys[i]:
            i += 1
        if i < len(current_node.keys) and current_node.keys[i] == key:
            print(f"Key {key} found in node: {current_node.keys}")
            return True
        if current_node.leaf:
            print(f"Key {key} not found.")
            return False
        return self.search(key, current_node.children[i])

