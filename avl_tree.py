"""
An ordered symbol table implementation of key-value pairs. The implemented
symbol table supports the following operations.

is_empty():
    Check whether this symbol table is empty or not.

size():
    Return the number of key-value pairs in the symbol table.

height():
    Computes the height of the AVL Tree with the convention that the height of
    a empty subtree is -1 and subtree with one element is 0.

contains(key):
    Check whether the symbol table contains the given key or not.

get(key):
    Returns the value associated with the given key in the table or None if no
    such key.

put(key, value):
    Inserts the key-value pair into the symbol table. It overwrites the old
    value with the new value if the key is already in the symbol table. If the
    value is 'None', this effectively deletes the key from the table.

delete(key):
    Remove the given key and the associated value with it from the table.

floor(key):
    Returns the largest key less than or equal to given key in the table.

ceiling(key):
    Returns the smallest key greater than or equal to given key in the table.

select(k):
    Returns the kth smallest key in the symbol table.

rank(key):
    Returns the number of keys in the table strictly less than key.

delete_min():
    Removes the smallest key and the associated value with it from the table.

delete_max():
    Removes the largest key and the associated value with it from the table.

max():
    Reutrns the largest key in the Symbol table

min():
    Reutrns the smallest key in the Symbol table

keys():
    Returns all keys in the symbol table.

keys_inorder():
    Returns all keys in the table following the in-order traversal.

keys_level_order():
    Returns all keys in the table following the in-order traversal.

keys_inrange(low_key, high_key):
    Returns all keys in between low_key and high_key (exclusive).

size_inrange(low_key, high_key):
    Returns the number of keys in in between low_key and high_key.

******************************************************************************

It also support the following operations to check the internal integrities of
the AVL tree.

checked():
    Check if all the representational invariantsis are consistent.

is_AVL():
    Check if the AVL property of the tree is consistent.

is_BST():
    Check if the BST property of the tree is consistent.

is_size_consistent():
    Check if the size of the AVL tree is consistent.

is_rank_consistent():
    Check if the rank of the AVL tree is consistent.

"""
import sys
from random import randrange


class AVLTreeST(object):
    """Symbol table implementation using AVL tree.

    The class represents an ordered symbol table of generic key-value pairs.
    A symbol table implements the associative array abstraction: when
    associating a value with a key that is already in the symbol table, the
    convention is to replace the old value with the new value. Setting the
    value associated with a key to None is equivalent to deleting the key from
    the symbol table.

    The implementation uses AVL tree (https://en.wikipedia.org/wiki/AVL_tree),
    which is a self-balancing BST. In an AVL tree, the heights of the two
    child subtrees of any node differ by at most one; if at any time
    they differ by more than one, re-balancing is done to restore this
    property.
    """

    # *************************** Nested Node Class ***************************#
    class Node(object):
        def __init__(self, key, value, size, height, left=None, right=None):
            self.key = key  # the key
            self.value = value  # the value associated with the key
            self.left = left  # left subtree
            self.right = right  # right subtree
            self.size = size  # number of subtree rooted at this tree
            self.height = height  # height of the subtree

        def __iter__(self):
            yield from self.left if self.left is not None else ()
            yield self.key
            yield from self.right if self.right is not None else ()

    # ************************ End of Nested Node Class ***********************#

    def __init__(self):
        """ It initializes an ordered symbol table. """
        self.root = None

    def is_empty(self):
        """ Check whether this symbol table is empty or not. """
        return self.root is None

    def size(self):
        """ Return the number of key-value pairs in the symbol table. """
        return self._size(self.root)

    def _size(self, x):
        """ Return the number of elements in the subtree. """
        if x is None:
            return 0
        else:
            return x.size

    def height(self):
        """Computes the height of the AVL tree.

        The convention is that the height of a empty subtree is -1 and subtree
        with one element is 0.

        Returns:
            the height of the tree.
        """
        return self._height(self.root)

    def _height(self, x):
        """Return the height of the given subtree.
        Args:
            x: the subtree
        """
        if x is None:
            return -1
        return x.height

    def contains(self, key):
        """Check whether the symbol table contains the given key or not.

        Args:
            key: the key to check if it is in the table
        Returns:
            True if the tree contains the given key or False otherwise
        """
        if key is None:
            raise ValueError("Can't search 'None'")
        return self.get(key) is not None

    def get(self, key):
        """Returns the value associated with given key or None if no such key.

        Args:
            key: the key of which value to be gotten
        Returns:
            value associated with the given key if the key is in the table and
            None if the key is not in the table.
        """
        if key is None:
            raise ValueError("Can't search 'None' in the table")
        x = self._get(self.root, key)
        if x is None:
            return None
        return x.value

    def _get(self, x, key):
        """Return the subtree associate with the given key.

        Args:
            x  : the subtree
            key: the key with which a value is associated
        Returns:
            subtree corresponding to the given key if the key is in the tree and
            None if the key is not in the symbol table.
        """
        if x is None:
            return None
        elif key < x.key:
            return self._get(x.left, key)
        elif key > x.key:
            return self._get(x.right, key)
        else:
            return x

    def put(self, key, value):
        """Inserts the key-value pair into the symbol table.

        It overwrites the old value with the new value if the key is already
        in the symbol table. If the value is None, this effectively deletes the
        key from the table.

        Args:
            key  : the key to be inserted into the table.
            value: value associated with the given key
        """
        if key is None:
            raise ValueError("Can't insert 'None' in the table")
        if value is None:
            self._delete(self.root, key)
            return
        self.root = self._put(self.root, key, value)
        assert self.checked()

    def _put(self, x, key, value):
        """Add the given key-value pair in the subtree rooted at x.

        If the key is already in the tree, its value gets updated.

        Args:
            x    : the subtree
            key  : the key to be inserted into the symbol table.
            value: value associated with the given key
        """
        if x is None:
            return self.Node(key, value, 1, 0)
        if key < x.key:
            x.left = self._put(x.left, key, value)
        elif key > x.key:
            x.right = self._put(x.right, key, value)
        else:
            x.value = value
            return x
        x.size = 1 + self._size(x.left) + self._size(x.right)
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return self._balance(x)

    def _balance_factor(self, x):
        """Compute the difference in height of two children of the subtree, x.

        The balance factor is positive if the height of left subtree of x is
        greater than its right subtree, zero if they are equal, or negative
        otherwise.
        """
        return self._height(x.left) - self._height(x.right)

    def _balance(self, x):
        """Balance the given subtree x if it violates AVL Tree property.

        Args:
            x: a subtree
        Return:
            the subtree with restored AVL Tree property
        """
        if self._balance_factor(x) < -1:
            if self._balance_factor(x.right) > 0:
                x.right = self._rotate_right(x.right)
            x = self._rotate_left(x)
        elif self._balance_factor(x) > 1:
            if self._balance_factor(x.left) < 0:
                x.left = self._rotate_left(x.left)
            x = self._rotate_right(x)

        return x

    def _rotate_right(self, x):
        """Rotate the given subtree (x) to the right.

        Args:
            x: a subtree
        Return:
            the right rotated subtree.
        """
        y = x.left
        x.left = y.right
        y.right = x
        y.size = x.size
        x.size = 1 + self._size(x.left) + self._size(x.right)
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _rotate_left(self, x):
        """Rotate the given subtree (x) to the left.

        Args:
            x: a subtree
        Returns:
            the left rotated subtree
        """
        y = x.right
        x.right = y.left
        y.left = x
        y.size = x.size
        x.size = 1 + self._size(x.left) + self._size(x.right)
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def delete(self, key):
        """Remove the given key and associated value with it from the table.

        Args:
            key: the key to be removed
        """
        if key is None:
            raise ValueError("Can't delete 'None' from the table")
        if not self.contains(key):
            return
        self.root = self._delete(self.root, key)

    def _delete(self, x, key):
        """Remove the given key and associated value with it from the table.

        Args:
            x  : the subtree
            key: the key to be removed from the tree
        Returns:
            The updated subtree
        """
        if x is None:
            return
        elif key < x.key:
            x.left = self._delete(x.left, key)
        elif key > x.key:
            x.right = self._delete(x.right, key)
        else:
            if x.left is None:
                return x.right
            elif x.right is None:
                return x.left
            else:
                y = x
                x = self._min(y.right)
                x.right = self._delete_min(y.right)
                x.left = y.left

        x.size = 1 + self._size(x.left) + self._size(x.right)
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return self._balance(x)

    def delete_min(self):
        """Removes the smallest key and its value from the table."""
        if self.is_empty():
            raise RuntimeError(" delete_min() is called on empty table")
        self.root = self._delete_min(self.root)

    def _delete_min(self, x):
        """Delete the minimum key and its value from the table.

        Args:
            x: the subtree
        Returns:
            The updated subtree
        """
        if x.left is None:
            return x.right
        x.left = self._delete_min(x.left)
        x.size = 1 + self._size(x.left) + self._size(x.right)
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return self._balance(x)

    def delete_max(self):
        """Remove the largest key and its value from the symbol table"""
        if self.is_empty():
            return RuntimeError(" delete_max() is called on empty table")
        self.root = self._delete_max(self.root)

    def _delete_max(self, x):
        """Remove the largest key and its value from the given subtree

        Args:
            x: the subtree

        Returns:
            updated subtree (Node Object)
        """
        if x.right is None:
            return x.right
        x.right = self._delete_max(x.right)
        x.size = 1 + self._size(x.left) + self._size(x.right)
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return self._balance(x)

    def max(self):
        """Reutrns the largest key in the Symbol table"""
        if self.is_empty():
            return RuntimeError(" max() is called in empty table")
        return self._max(self.root)

    def _max(self, x):
        """Reutrns the subtree with the largest key in the table"""
        if x.right is None:
            return x
        else:
            return self._max(x.right)

    def min(self):
        """Reutrns the smallest key in the Symbol table"""
        if self.is_empty():
            return RuntimeError(" min() is called in empty table")
        return self._min(self.root)

    def _min(self, x):
        """Reutrns the subtree with the smallest key in the Symbol table"""
        if x.left is None:
            return x
        else:
            return self._min(x.left)

    def floor(self, key):
        """Returns the largest key less than or equal to the given key.

        Args:
            key  : the key
        Returns:
            the largest key less than or equal to the given key.
        """
        if key is None:
            raise ValueError("Can't search 'None' in the table")
        if self.is_empty():
            raise RuntimeError(" floor(key) is called on empty table")
        x = self._floor(self.root, key)
        if x is None:
            return None
        return x.key

    def _floor(self, x, key):
        """Returns the subtree with the largest key ≤ the given key.

        Args:
            x  : the subtree
            key: the key

        Returns:
            subtree with the largest key less than or equal to the given key.
        """
        if x is None:
            return None
        elif key == x.key:
            return x
        elif key < x.key:
            return self._floor(x.left, key)
        y = self._floor(x.right, key)
        if y is not None:
            return y
        else:
            return x

    def ceiling(self, key):
        """Returns the smallest key greater than or equal to the given key.

        Args:
            key  : the key

        Returns:
            the smallest key greater than or equal to the given key
        """
        if key is None:
            raise ValueError("Can't search 'None' from the table")
        if self.is_empty():
            raise RuntimeError("ceiling(key) is called on empty table")
        x = self._ceiling(self.root, key)
        if x is None:
            return None
        return x.key

    def _ceiling(self, x, key):
        """Returns the subtree with the smallest key ≥ the given key.

        Args:
            x  : the subtree
            key: the key

        Returns:
            subtree with the smallest key greater than or equal to given key.
        """
        if x is None:
            return None
        if key == x.key:
            return x
        if key > x.key:
            return self._ceiling(x.right, key)
        y = self._ceiling(x.left, key)
        if y is not None:
            return y
        else:
            return x

    def select(self, k):
        """Returns the kth smallest key in the symbol table.

        Args:
            K: the order statistic

        Returns:
            the kth smallest key in the table.
        """
        if k < 0 or k >= self.size():
            raise ValueError("k is out of range")
        x = self._select(self.root, k)
        return x.key

    def _select(self, x, k):
        """Returns the subtree with the kth smallest key.

        Args:
            x: the subtree
            k: the kth smallest key in the subtree

        Returns:
            the subtree with the kth smallest key
        """
        if x is None:
            return None
        elif k < self._size(x.left):
            return self._select(x.left, k)
        elif k > self._size(x.left):
            return self._select(x.right, (k - self._size(x.left)) - 1)
        else:
            return x

    def rank(self, key):
        """Returns the number of keys in the table strictly less than key.

        Args:
            key: the key

        Returns:
            the number of keys in the table strictly less than key.
        """
        if key is None:
            raise ValueError("key can't be 'None'")
        return self._rank(self.root, key)

    def _rank(self, x, key):
        """Returns the number of keys in the subtree less than key.

        Args:
            x  : the subtree
            key: the key

        Returns:
            the number of keys in the subtree less than key.
        """
        if x is None:
            return 0
        elif key < x.key:
            return self._rank(x.left, key)
        elif key > x.key:
            return 1 + self._size(x.left) + self._rank(x.right, key)
        else:
            return self._size(x.left)

    def keys(self):
        """Returns all keys in the symbol table.

        Returns:
            an iterable containing all keys in the symbol table.
        """
        return self.keys_inorder()

    def keys_inorder(self):
        """Returns all keys in the table following the in-order traversal.

        Returns:
            an iterable containing all keys in the table.
        """
        q = []
        self._keys_inorder(self.root, q)
        return q

    def _keys_inorder(self, x, queue):
        """Adds the keys to queue following an in-order traversal.

        Args:
            x    : the subtree
            queue: the queue to hold the keys.
        """
        if x is None:
            return
        self._keys_inorder(x.left, queue)
        queue.append(x.key)
        self._keys_inorder(x.right, queue)

    def keys_level_order(self):
        """Returns all keys in the table following the in-order traversal.

        Returns:
            an iterable containing all keys in the table.
        """
        q1 = []
        if not self.is_empty():
            q2 = []
            q2.append(self.root)
            while len(q2) > 0:
                x = q2.pop(0)
                q1.append(x.key)
                if x.left is not None:
                    q2.append(x.left)
                if x.right is not None:
                    q2.append(x.right)

        return q1

    def keys_inrange(self, low_key, high_key):
        """Returns all keys in between low_key and high_key (exclusive).

        Args:
            low_key : the lowest key
            high_key: the highest key

        Returns:
            an iterable containing all keys in between low_key (inclusive)
            and high_key (exclusive)
        """
        if low_key is None:
            raise ValueError("keys can't be 'None'")
        if high_key is None:
            raise ValueError("keys can't be 'None'")
        q = []
        self._keys_inrange(self.root, q, low_key, high_key)
        return q

    def _keys_inrange(self, x, q, low_key, high_key):
        """Returns all keys in between low_key and high_key as iterable.

        Args:
            x       : the subtree
            queue   : the queue to hold the keys
            low_key : the lowest key
            high_key: the highest key
        """
        if x is None:
            return None
        if low_key < x.key:
            self._keys_inrange(x.left, q, low_key, high_key)
        if low_key == x.key and high_key >= x.key:
            q.append(x.key)
        if high_key > x.key:
            self._keys_inrange(x.right, q, low_key, high_key)

    def size_inrange(self, low_key, high_key):
        """Returns the number of keys in in between low_key and high_key.

        Args:
            low_key : the lowest key
            high_key: the highest key

        Returns:
            the number of keys in between low_key (inclusive) and
            high_key (inclusive)
        """
        if low_key is None:
            raise ValueError("keys can't be 'None'")
        if high_key is None:
            raise ValueError("keys can't be 'None'")
        if low_key > high_key:
            return 0
        if self.contains(high_key):
            return self.rank(high_key) - self.rank(low_key) + 1
        return self.rank(high_key) - self.rank(low_key)

    def checked(self):
        """Check if all the representational invariantsis are consistent.

        Returns:
            True if all the representational invariantsis are consistent or
            False otherwise.
        """
        if not self.is_BST():
            print("Symmetric order not consistent")
        if not self.is_AVL():
            print("AVL property not consistent")
        if not self.is_size_consistent():
            print("Subtree counts not consistent")
        if not self.is_rank_consistent():
            print("Ranks not consistent")
        return (
            self.is_BST()
            and self.is_AVL()
            and self.is_size_consistent()
            and self.is_rank_consistent()
        )

    def is_AVL(self):
        """Check if the AVL property of the tree is consistent.

        Returns:
            True if AVL property is consistent or False otherwise.
        """
        return self._is_AVL(self.root)

    def _is_AVL(self, x):
        """Check if the AVL property of the subtree is consistent.

        Args:
            x: the subtree

        Returns:
            True if AVL property is consistent or False otherwise.
        """
        if x is None:
            return True
        bf = self._balance_factor(x)
        if bf < -1 or bf > 1:
            return False
        else:
            return self._is_AVL(x.left) and self._is_AVL(x.right)

    def is_BST(self):
        """Check if the BST property of the tree is consistent.

        Returns:
            True if BST property is consistent or False otherwise.
        """
        return self._is_BST(self.root, None, None)

    def _is_BST(self, x, smaller, larger):
        """Check if the BST property of the subtree (x) is consistent.

        Args:
            x: the subtree

        Returns:
            True if BST property of subtree is consistent or False otherwise.
        """
        if x is None:
            return True
        if smaller is not None and x.key <= smaller:
            return False
        if larger is not None and x.key >= larger:
            return False
        return self._is_BST(x.left, smaller, x.key) and self._is_BST(
            x.right, x.key, larger
        )

    def is_size_consistent(self):
        """Check if the size of the AVL tree is consistent.

        Returns:
            True if the size of the AVL tree is consistent or False otherwise.
        """
        return self._is_size_consistent(self.root)

    def _is_size_consistent(self, x):
        """Check if the size of the subtree (x) is consistent.

        Args:
            x: the subtree

        Returns:
            True if the size of the subtree is consistent or False otherwise.
        """
        if x is None:
            return True
        if self._size(x) != 1 + self._size(x.left) + self._size(x.right):
            return False
        return self._is_size_consistent(x.left) and self._is_size_consistent(x.right)

    def is_rank_consistent(self):
        """Check if the rank of the AVL tree is consistent.

        Returns:
            True if the rank of the AVL tree is consistent or False otherwise.
        """
        for i in range(self.size()):
            if i != self.rank(self.select(i)):
                return False
        for key in self.keys():
            if key != self.select(self.rank(key)):
                return False
        return True

    # ************************ Python Special Methods: ************************#
    def __len__(self):
        return self.size()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self.contains(key)

    def __delitem__(self, key):
        self.delete(key)

    def __iter__(self):
        if self.root is not None:
            return iter(self.root)
        else:
            return iter([])

    # ********************* End of Python Special Methods *********************#
