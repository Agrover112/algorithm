#!/usr/bin/env ipython
import unittest
from os_tree import os_tree, os_node


class TestOstree(unittest.TestCase):
    def test_insert_one(self):
        T = os_tree([41])
        print(T.root.iterative_tree_search(41).p.key)
        self.assertEqual(T.root, T.root.iterative_tree_search(41))
        self.assertEqual(T.nil.size, 0)
        self.wrap(T, 41, -1, -1, -1, 1, 1)

    def test_insert_two(self):
        T = os_tree([41, 38])
        self.assertEqual(T.root, T.iterative_tree_search(41))
        self.assertEqual(T.nil.size, 0)
        self.wrap(T, 41, 38, -1, -1, 1, 2)
        self.wrap(T, 38, -1, -1, 41, 0, 1)

    def test_insert_three(self):
        T = os_tree([41, 38, 31])
        self.assertEqual(T.root, T.iterative_tree_search(38))
        self.assertEqual(T.nil.size, 0)
        self.wrap(T, 38, 31, 41, -1, 1, 3)
        self.wrap(T, 31, -1, -1, 38, 0, 1)
        self.wrap(T, 41, -1, -1, 38, 0, 1)

    def test_insert_four(self):
        T = os_tree([41, 38, 31, 12])
        self.assertEqual(T.root, T.iterative_tree_search(38))
        self.assertEqual(T.nil.size, 0)
        self.wrap(T, 38, 31, 41, -1, 1, 4)
        self.wrap(T, 31, 12, -1, 38, 1, 2)
        self.wrap(T, 41, -1, -1, 38, 1, 1)
        self.wrap(T, 12, -1, -1, 31, 0, 1)

    def test_insert_five(self):
        T = os_tree([41, 38, 31, 12, 19])
        self.assertEqual(T.root, T.iterative_tree_search(38))
        self.assertEqual(T.nil.size, 0)
        self.wrap(T, 38, 19, 41, -1, 1, 5)
        self.wrap(T, 19, 12, 31, 38, 1, 3)
        self.wrap(T, 41, -1, -1, 38, 1, 1)
        self.wrap(T, 12, -1, -1, 19, 0, 1)
        self.wrap(T, 31, -1, -1, 19, 0, 1)

    def test_insert_six(self):
        T = os_tree([41, 38, 31, 12, 19, 9])
        self.assertEqual(T.root, T.iterative_tree_search(38))
        self.assertEqual(T.nil.size, 0)
        self.wrap(T, 38, 19, 41, -1, 1, 6)
        self.wrap(T, 19, 12, 31, 38, 0, 4)
        self.wrap(T, 41, -1, -1, 38, 1, 1)
        self.wrap(T, 12, 9, -1, 19, 1, 2)
        self.wrap(T, 31, -1, -1, 19, 1, 1)
        self.wrap(T, 9, -1, -1, 12, 0, 1)

    def test_delete_one(self):
        T = os_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        self.wrap(T, 38, 19, 41, -1, 1, 5)
        self.wrap(T, 19, 12, 31, 38, 0, 3)
        self.wrap(T, 41, -1, -1, 38, 1, 1)
        self.wrap(T, 12, -1, -1, 19, 1, 1)
        self.wrap(T, 31, -1, -1, 19, 1, 1)

    def test_delete_two(self):
        T = os_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        self.wrap(T, 38, 19, 41, -1, 1, 4)
        self.wrap(T, 19, -1, 31, 38, 1, 2)
        self.wrap(T, 41, -1, -1, 38, 1, 1)
        self.wrap(T, 31, -1, -1, 19, 0, 1)

    def test_delete_three(self):
        T = os_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        self.wrap(T, 38, 31, 41, -1, 1, 3)
        self.wrap(T, 31, -1, -1, 38, 1, 1)
        self.wrap(T, 41, -1, -1, 38, 1, 1)

    def test_delete_four(self):
        T = os_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        self.wrap(T, 38, -1, 41, -1, 1, 2)
        self.wrap(T, 41, -1, -1, 38, 0, 1)

    def test_delete_five(self):
        T = os_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        self.wrap(T, 41, -1, -1, -1, 1, 1)

    def test_delete_six(self):
        T = os_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        T.delete(T.iterative_tree_search(41))
        self.assertEqual(T.root, T.nil)
        self.assertEqual(T.nil.size, 0)

    def test_key_rank(self):
        T = os_tree([41, 38, 31, 12, 19, 9])
        self.assertEqual(T.root.key_rank(41), 6)
        self.assertEqual(T.root.key_rank(38), 5)
        self.assertEqual(T.root.key_rank(31), 4)
        self.assertEqual(T.root.key_rank(12), 2)
        self.assertEqual(T.root.key_rank(19), 3)
        self.assertEqual(T.root.key_rank(9), 1)

    def test_rank(self):
        T = os_tree([41, 38, 31, 12, 19, 9])
        self.assertEqual(T.rank(T.iterative_tree_search(41)), 6)
        self.assertEqual(T.rank(T.iterative_tree_search(38)), 5)
        self.assertEqual(T.rank(T.iterative_tree_search(31)), 4)
        self.assertEqual(T.rank(T.iterative_tree_search(12)), 2)
        self.assertEqual(T.rank(T.iterative_tree_search(19)), 3)
        self.assertEqual(T.rank(T.iterative_tree_search(9)), 1)

    def test_select(self):
        T = os_tree([41, 38, 31, 12, 19, 9])
        self.assertEqual(T.root.select_recursive(1).key, 9)
        self.assertEqual(T.root.select_recursive(2).key, 12)
        self.assertEqual(T.root.select_recursive(3).key, 19)
        self.assertEqual(T.root.select_recursive(4).key, 31)
        self.assertEqual(T.root.select_recursive(5).key, 38)
        self.assertEqual(T.root.select_recursive(6).key, 41)
        self.assertEqual(T.root.select_iterative(1).key, 9)
        self.assertEqual(T.root.select_iterative(2).key, 12)
        self.assertEqual(T.root.select_iterative(3).key, 19)
        self.assertEqual(T.root.select_iterative(4).key, 31)
        self.assertEqual(T.root.select_iterative(5).key, 38)
        self.assertEqual(T.root.select_iterative(6).key, 41)

    def test_ith_successor(self):
        T = os_tree([41, 38, 31, 12, 19, 9])
        self.assertEqual(T.iterative_tree_search(9).ith_successor(1).key, 12)
        self.assertEqual(T.iterative_tree_search(9).ith_successor(2).key, 19)
        self.assertEqual(T.iterative_tree_search(9).ith_successor(3).key, 31)
        self.assertEqual(T.iterative_tree_search(9).ith_successor(4).key, 38)
        self.assertEqual(T.iterative_tree_search(9).ith_successor(5).key, 41)

    #    def test_insert_stack(self):
    #        T = os_tree([])
    #        for i in 41, 38, 31, 12, 19, 9:
    #            T.insert_stack(os_node(i, None, None, None, 0))
    #        self.assertEqual(T.root, T.iterative_tree_search(38))
    #        self.assertEqual(T.nil.color, 1)
    #        self.wrap(T, 38, 19, 41, -1, 1)
    #        self.wrap(T, 19, 12, 31, 38, 0)
    #        self.wrap(T, 41, -1, -1, 38, 1)
    #        self.wrap(T, 12, 9, -1, 19, 1)
    #        self.wrap(T, 31, -1, -1, 19, 1)
    #        self.wrap(T, 9, -1, -1, 12, 0)
    def wrap(self, tree, node, left, right, p, color, size):
        self.assertEqual(tree.iterative_tree_search(node).left, tree.iterative_tree_search(left))
        self.assertEqual(tree.iterative_tree_search(node).right, tree.iterative_tree_search(right))
        self.assertEqual(tree.iterative_tree_search(node).p, tree.iterative_tree_search(p))
        self.assertEqual(tree.iterative_tree_search(node).color, color)
        self.assertEqual(tree.iterative_tree_search(node).size, size)


if __name__ == '__main__':
    unittest.main()
