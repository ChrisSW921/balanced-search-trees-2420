"""Binary search tree"""

from recursioncounter import RecursionCounter


class Node:
    """Node Class"""
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.height = 0

    def is_leaf(self):
        """Checks if node is leaf"""
        return bool(not self.left_child and not self.right_child)

    def update_height(self):
        """Update height"""
        left_child_height = -1
        right_child_height = -1
        if self.left_child is not None:
            left_child_height = self.left_child.height
        if self.right_child is not None:
            right_child_height = self.right_child.height
        self.height = max(left_child_height, right_child_height) + 1

    def __str__(self):
        """str function"""
        return f"Node({self.data})"


class BinarySearchTree:
    """Binary Search Tree class"""
    def __init__(self):
        self.root = None

    def is_empty(self):
        """Checks if tree is empty"""
        return self.root is None

    def add(self, data):
        """Add function"""
        lyst = self.inorder()
        if data in lyst:
            pass
        else:
            self.root = self.add_helper(self.root, data)

    def add_helper(self, cursor, data):
        """Add helper"""
        RecursionCounter()

        if cursor is None:
            return Node(data)

        if data < cursor.data:
            cursor.left_child = self.add_helper(cursor.left_child, data)

        else:
            cursor.right_child = self.add_helper(cursor.right_child, data)

        cursor.update_height()

        return cursor

    def find(self, data):
        """Find"""
        return self.find_helper(self.root, data)

    def find_helper(self, cursor, data):
        """Find helper"""
        RecursionCounter()

        if cursor is None:
            return None

        if cursor.data == data:
            return cursor

        if data < cursor.data:
            return self.find_helper(cursor.left_child, data)
        else:
            return self.find_helper(cursor.right_child, data)

    def remove(self, data):
        """Remove"""
        self.root = self.remove_helper(self.root, data)

    def remove_helper(self, cursor, data):
        """Remove helper"""
        RecursionCounter()

        if cursor is None:
            return None

        if cursor.data == data:
            if cursor.is_leaf():
                return None
            if cursor.right_child is None:
                return cursor.left_child
            if cursor.left_child is None:
                return cursor.right_child
            successor = cursor.right_child
            while successor.left_child is not None:
                successor = successor.left_child

            cursor.data = successor.data
            cursor.right_child = self.remove_helper(cursor.right_child, successor.data)
            cursor.update_height()

            return cursor

        if data < cursor.data:
            cursor.left_child = self.remove_helper(cursor.left_child, data)
        else:
            cursor.right_child = self.remove_helper(cursor.right_child, data)

        cursor.update_height()
        return cursor

    def __len__(self):
        """len """
        return self.length_helper(self.root)

    def length_helper(self, cursor):
        """Len helper"""
        RecursionCounter()

        if cursor is None:
            return 0
        return 1 + self.length_helper(cursor.left_child) + self.length_helper(cursor.right_child)

    def __str__(self):
        """Str"""
        offset = ""
        tmp = self.print_helper(self.root, offset)
        return tmp

    def print_helper(self, cursor, offset):
        """Str helper"""
        RecursionCounter()

        if cursor is None:
            return offset + "[Empty]\n"
        if cursor.is_leaf():
            return f"{offset}{cursor.data} ({cursor.height}) [leaf]\n"

        return f"{offset}{cursor.data} ({cursor.height})\n" + \
        self.print_helper(cursor.left_child, offset + "  ") + \
        self.print_helper(cursor.right_child, offset + "  ")

    def preorder(self):
        """Pre order"""
        output = []
        self.preorder_helper(self.root, output)
        return output

    def preorder_helper(self, cursor, output):
        """Pre order helper"""
        RecursionCounter()

        if cursor is None:
            return

        output.append(cursor.data)
        self.preorder_helper(cursor.left_child, output)
        self.preorder_helper(cursor.right_child, output)

    def height(self):
        """Height"""
        if self.root is None:
            return -1
        return self.root.height

    def inorder(self, root="empty"):
        """In order"""
        if root == "empty":
            root = self.root
            return (self.inorder(root.left_child) + [root.data] + self.inorder(root.right_child)) if root else []
        else:
            return (self.inorder(root.left_child) + [root.data] + self.inorder(root.right_child)) if root else []

    def rebalance_tree(self):
        """Rebalance tree"""
        lyst = self.inorder()
        self.root = None
        midpoint = int(len(lyst) / 2)
        left = lyst[:midpoint].copy()
        right = lyst[midpoint + 1:].copy()
        root = lyst.pop(midpoint)

        def recursor(left, right):
            """Rebalance helper"""
            RecursionCounter()
            if len(left) > 0:
                mid_left = int(len(left) / 2)
                left_lyst = left[:mid_left].copy()
                right_lyst = left[mid_left + 1:].copy()
                left_item = left.pop(mid_left)
                self.add(left_item)
                recursor(left_lyst, right_lyst)
            if len(right) > 0:
                mid_right = int(len(right) / 2)
                left_lyst = right[:mid_right].copy()
                right_lyst = right[mid_right + 1:].copy()
                right_item = right.pop(mid_right)
                self.add(right_item)
                recursor(left_lyst, right_lyst)

        self.add(root)
        recursor(left, right)














        # if not arr:
        #     return None
        #
        # if arr == "m":
        #     arr = self.inorder()
        #     mid = len(arr) // 2
        #     self.root = Node(arr[mid])
        #
        # mid = len(arr) // 2
        # print(f"mid {mid}")
        # # make the middle element the root
        # new_root = Node(arr[mid])
        #
        # # left subtree of root has all
        # # values <arr[mid]
        # print(arr)
        # new_root.left = self.rebalance_tree(arr[:mid])
        #
        # # right subtree of root has all
        # # values >arr[mid]
        # new_root.right = self.rebalance_tree(arr[mid + 1:])
        #
        # return self.root






