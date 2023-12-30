"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack


class TestStack(unittest.TestCase):

    def test_stack(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.top.data, "data3")
        self.assertEqual(stack.top.next_node.data, "data2")
        self.assertEqual(stack.top.next_node.next_node.data, "data1")
        self.assertEqual(stack.top.next_node.next_node.next_node, None)

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.pop(), "data3")
        self.assertEqual(stack.pop(), "data2")
        self.assertEqual(stack.pop(), "data1")
        # self.assertEqual(stack.pop(), None)
