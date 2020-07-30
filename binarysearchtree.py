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
        left_child_height = -1
        right_child_height = -1
        if self.left_child is not None:
            left_child_height = self.left_child.height
        if self.right_child is not None:
            right_child_height = self.right_child.height
        self.height = max(left_child_height, right_child_height) + 1

    def __str__(self):
        return f"Node({self.data})"



class BinarySearchTree:
    """Binary Search Tree class"""
    def __init__(self):
        self.root = None

    def is_empty(self):
        """Checks if tree is empty"""
        return self.root is None

    def add(self, data):
        lyst = self.inorder()
        if data in lyst:
            pass
        else:
            self.root = self.add_helper(self.root, data)

    def add_helper(self, cursor, data):
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
        return self.find_helper(self.root, data)

    def find_helper(self, cursor, data):
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
        self.root = self.remove_helper(self.root, data)

    def remove_helper(self, cursor, data):
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
        return self.length_helper(self.root)

    def length_helper(self, cursor):
        RecursionCounter()

        if cursor is None:
            return 0
        return 1 + self.length_helper(cursor.left_child) + self.length_helper(cursor.right_child)

    def __str__(self):
        offset = ""
        tmp = self.print_helper(self.root, offset)
        return tmp

    def print_helper(self, cursor, offset):
        RecursionCounter()

        if cursor is None:
            return offset + "[Empty]\n"
        if cursor.is_leaf():
            return f"{offset}{cursor.data} ({cursor.height}) [leaf]\n"

        return f"{offset}{cursor.data} ({cursor.height})\n" + \
        self.print_helper(cursor.left_child, offset + "  ") + \
        self.print_helper(cursor.right_child, offset + "  ")

    def preorder(self):
        output = []
        self.preorder_helper(self.root, output)
        return output

    def preorder_helper(self, cursor, output):
        RecursionCounter()

        if cursor is None:
            return

        output.append(cursor.data)
        self.preorder_helper(cursor.left_child, output)
        self.preorder_helper(cursor.right_child, output)

    def height(self):
        if self.root is None:
            return -1
        return self.root.height

    def inorder(self, root="empty"):
        if root == "empty":
            root = self.root
            return (self.inorder(root.left_child) + [root.data] + self.inorder(root.right_child)) if root else []
        else:
            return (self.inorder(root.left_child) + [root.data] + self.inorder(root.right_child)) if root else []


    def rebalance_tree(self, arr="No arr"):

        if arr == "No arr":
            arr = self.inorder()

        if not arr:
            return None

        # find middle
        mid = (len(arr)) // 2

        # make the middle element the root
        self.root = Node(arr[mid])

        # left subtree of root has all
        # values <arr[mid]
        self.root.left_child = self.rebalance_tree(arr[:mid])

        # right subtree of root has all
        # values >arr[mid]
        self.root.right_child = self.rebalance_tree(arr[mid + 1:])
        return self.root

    # def __len__(self, counter=0):
    #     """Length function"""
    #     if counter < 40:
    #         RecursionCounter()
    #         self.__len__(counter + 1)
    #     else:
    #         pass
    #     return self.size
    #
    # def height(self, start=None):
    #     """Returns the height of the tree"""
    #     lyst = []
    #     if start is None:
    #         start = self.root
    #
    #     def max_depth(node, count=0):
    #         """Helper recursive function for the height function"""
    #         RecursionCounter()
    #         if node is None:
    #             return 0
    #         else:
    #             lyst.append(count)
    #             l_depth = (max_depth(node.left_child, count + 1))
    #             r_depth = (max_depth(node.right_child, count + 1))
    #             return max(lyst)
    #
    #     return max_depth(start)
    #
    # def __str__(self):
    #     """Returns a string representation of the binary search tree"""
    #
    #     def str_helper(node, indent=0):
    #         """Recursive helper function for the str method"""
    #         result = ''
    #         if node is not None:
    #             item = str(node.data)
    #             below = self.height(node)
    #             tab = ''
    #             for i in range(indent):
    #                 tab += '\t'
    #             result += tab + item
    #             result += ' (' + str(below) + ')'
    #             if below == 0:
    #                 result += "[Leaf]"
    #             result += '\n'
    #             if node.left_child is None and below != 0:
    #                 tab += '\t'
    #                 result += tab + "[Empty]" + '\n'
    #             result += str_helper(node.left_child, indent + 1)
    #             if node.right_child is None and below != 0:
    #                 tab += '\t'
    #                 result += tab + "[Empty]" + '\n'
    #             result += str_helper(node.right_child, indent + 1)
    #         return result
    #
    #     return str_helper(self.root)
    #
    #
    # def add(self, item):
    #     """Add function"""
    #     def add_helper(node):
    #         """Add helper"""
    #         RecursionCounter()
    #         if item < node.data:
    #             if node.left_child is None:
    #                 node.left_child = Node(item)
    #             else:
    #                 add_helper(node.left_child)
    #         elif node.right_child is None:
    #             node.right_child = Node(item)
    #         else:
    #             add_helper(node.right_child)
    #     if self.find(item) is None:
    #         if self.is_empty():
    #             self.root = Node(item)
    #         else:
    #             add_helper(self.root)
    #         self.size += 1
    #
    #
    #
    # def remove(self, item):
    #     """Remove function"""
    #     self.parent = None
    #     self.search_parent = None
    #     self.count = 0
    #     self.parent_ref = None
    #     def remove_helper_2(item):
    #         """Remove helper 2"""
    #         if item.left_child and not item.right_child:
    #             self.parent_ref = item.left_child
    #         elif item.right_child and not item.left_child:
    #             self.parent_ref = item.right_child
    #         elif not item.right_child and not item.left_child:
    #             self.parent_ref = None
    #         else:
    #             left = item.left_child
    #             while left.right_child:
    #                 self.search_parent = left
    #                 left = left.right_child
    #                 self.count += 1
    #             else:
    #                 item.data = left.data
    #                 if self.count == 0:
    #                     item.left_child = item.left_child.left_child
    #                 else:
    #                     self.search_parent.right_child = self.search_parent.right_child.left_child
    #
    #     def remove_helper(item, new_root=None):
    #         """Recursive remove function"""
    #         RecursionCounter()
    #         if new_root:
    #             temp_root = new_root
    #         else:
    #             temp_root = self.root
    #         if temp_root.data == item:
    #             remove_helper_2(temp_root)
    #         elif item < temp_root.data:
    #             self.parent = temp_root
    #             self.parent_ref = self.parent.left_child
    #             remove_helper(item, temp_root.left_child)
    #         elif item > temp_root.data:
    #             self.parent = temp_root
    #             self.parent_ref = (self.parent.right_child)
    #             remove_helper(item, temp_root.right_child)
    #     self.size -= 1
    #     remove_helper(item)
    #
    # def find(self, item):
    #     """Find function"""
    #
    #     def find_helper(node):
    #         """Find helper function"""
    #         RecursionCounter()
    #         if node is None:
    #             return None
    #         elif item == node.data:
    #             return node.data
    #         elif item < node.data:
    #             return find_helper(node.left_child)
    #         else:
    #             return find_helper(node.right_child)
    #
    #     return find_helper(self.root)
    #
    # def preorder_helper(self, node=None, iter=0):
    #     """Preorder helper function"""
    #     RecursionCounter()
    #     if iter == 0:
    #         node = self.root
    #         if node is None:
    #             return
    #         self.pre_order.append(node.data)
    #         self.preorder_helper(node.left_child, 1)
    #         self.preorder_helper(node.right_child, 1)
    #     else:
    #         if node is None:
    #             return
    #         self.pre_order.append(node.data)
    #         self.preorder_helper(node.left_child, 1)
    #         self.preorder_helper(node.right_child, 1)
    #     return self.pre_order
    #
    # def preorder(self):
    #     """Preorder function"""
    #     self.preorder_helper()
    #     temp = self.pre_order.copy()
    #     self.pre_order.clear()
    #     return temp
    #
    # def inorder(self, root="empty"):
    #     if root == "empty":
    #         root = self.root
    #         return (self.inorder(root.left_child) + [root.data] + self.inorder(root.right_child)) if root else []
    #     else:
    #         return (self.inorder(root.left_child) + [root.data] + self.inorder(root.right_child)) if root else []
    #




