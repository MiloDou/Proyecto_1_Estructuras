
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
            # Ensure all ids are int for sorting
            current_node.keys.sort(key=lambda x: int(x.id))
        else:
            i = 0
            while i < len(current_node.keys) and int(key.id) > int(current_node.keys[i].id):
                i += 1
            if len(current_node.children[i].keys) == self.order - 1:
                self.split(current_node, i)
                if int(key.id) > int(current_node.keys[i].id):
                    i += 1
            self.insert_in_node(current_node.children[i], key)

    def split(self, parent_node, i):
        order = self.order
        child_node = parent_node.children[i]
        new_node = BNode(order)
        new_node.leaf = child_node.leaf
        middle = (order - 1) // 2
        middle_key = child_node.keys[middle]
        new_node.keys = child_node.keys[middle + 1:]
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
            print("Nivel", level, ":", [obj.id for obj in current_node.keys])
        for child in current_node.children:
            if child.keys or not child.leaf:
                self.display(child, level + 1)

    def search(self, key_id, current_node=None):
        if current_node is None:
            current_node = self.root
        i = 0
        while i < len(current_node.keys) and int(key_id) > int(current_node.keys[i].id):
            i += 1
        if i < len(current_node.keys) and int(current_node.keys[i].id) == int(key_id):
            print(f"Object with id {key_id} found in node: {[obj.id for obj in current_node.keys]}")
            return current_node.keys[i]
        if current_node.leaf:
            print(f"Object with id {key_id} not found.")
            return None
        return self.search(key_id, current_node.children[i])

