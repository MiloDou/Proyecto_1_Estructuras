class BNode:
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.children = []
        self.leaf = True

    def __str__(self):
        return f'Data: {self.keys} '
    