import unittest
from min_heap_with_linked_list import min_heap, min_priority_queue
from linked_list import linked_list, linked_list_node

class TestHeap(unittest.TestCase):
    def test_min_heapify(self):
        L1 = linked_list(1)
        L2 = linked_list(2)
        L2.insert(linked_list_node(2))
        L2.insert(linked_list_node(2))
        L3 = linked_list(3)
        L3.insert(linked_list_node(3))
        L3.insert(linked_list_node(3))
        L4 = linked_list(4)
        L4.insert(linked_list_node(4))
        L5 = linked_list(5)
        L3.insert(linked_list_node(5))
        L3.insert(linked_list_node(5))
        L3.insert(linked_list_node(5))
        h = min_heap([L5, L1, L2, L3, L4])
        h.min_heapify(0)
        self.assertEqual(h, [L1, L3, L2, L5, L4])
    def test_build_min_heap(self):
        L1 = linked_list(1)
        L2 = linked_list(2)
        L2.insert(linked_list_node(2))
        L2.insert(linked_list_node(2))
        L3 = linked_list(3)
        L3.insert(linked_list_node(3))
        L3.insert(linked_list_node(3))
        L4 = linked_list(4)
        L4.insert(linked_list_node(4))
        L5 = linked_list(5)
        L3.insert(linked_list_node(5))
        L3.insert(linked_list_node(5))
        L3.insert(linked_list_node(5))
        h = min_heap([L3, L4, L5, L2, L1])
        h.build_min_heap()
        self.assertEqual(h, [L1, L2, L5, L3, L4])
    def test_heap_minimum(self):
        L1 = linked_list(1)
        L1.insert(linked_list_node(1))
        L1.insert(linked_list_node(1))
        L2 = linked_list(2)
        L2.insert(linked_list_node(2))
        L2.insert(linked_list_node(2))
        L3 = linked_list(3)
        L3.insert(linked_list_node(3))
        L3.insert(linked_list_node(3))
        L4 = linked_list(4)
        L4.insert(linked_list_node(4))
        L5 = linked_list(5)
        L3.insert(linked_list_node(5))
        L3.insert(linked_list_node(5))
        L3.insert(linked_list_node(5))
        q = min_priority_queue([L1, L2, L3, L4, L5])
        self.assertEqual(q.heap_minimum().key, 1)
    def test_heap_extract_min(self):
        L1 = linked_list(1)
        L1.insert(linked_list_node(1))
        L1.insert(linked_list_node(1))
        L2 = linked_list(2)
        L2.insert(linked_list_node(2))
        L2.insert(linked_list_node(2))
        L3 = linked_list(3)
        L3.insert(linked_list_node(3))
        L3.insert(linked_list_node(3))
        L4 = linked_list(4)
        L4.insert(linked_list_node(4))
        L5 = linked_list(5)
        L3.insert(linked_list_node(5))
        L3.insert(linked_list_node(5))
        L3.insert(linked_list_node(5))
        q = min_priority_queue([L1, L2, L3, L4, L5])
        self.assertEqual(q.heap_extract_min().key, 1)
        self.assertEqual(q, [L1, L2, L3, L4, L5])
        self.assertEqual(q.heap_extract_min().key, 1)
        self.assertEqual(q, [L2, L4, L3, L5, L5])
#    def test_heap_decrease_key(self):
#        a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
#        q = min_priority_queue(a) 
#        q.heap_decrease_key(8, 1)
#        self.assertEqual(q, [1, 1, 3, 2, 7, 8, 9, 10, 4, 16])
#    def test_heap_insert(self):
#        a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
#        q = min_priority_queue(a)
#        q.heap_extract_min()
#        q.min_heap_insert(0)
#        self.assertEqual(q, [0, 2, 3, 10, 4, 8, 9, 16, 14, 7])
