"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest

from src.queue import Queue


class TestQueue(unittest.TestCase):

    def test_queue(self):
        queue = Queue()
        assert str(Queue()) == ""
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        # Проверяем очередность хранения данных
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertEqual(queue.tail.next_node, None)

    def test_str(self):
        queue = Queue()
        assert str(Queue()) == ""
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(str(queue), "data1\ndata2\ndata3")
