"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_linked_list_inserts(self):
        ll = LinkedList()
        assert str(ll) == "None"
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        assert str(ll) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        # метод to_list()
        lst = ll.to_list()
        assert lst == [{'id': 0, 'username': 'serebro'}, {'id': 1, 'username': 'lazzy508509'},
                       {'id': 2, 'username': 'mik.roz'}, {'id': 3, 'username': 'mosh_s'}]
        user_data = ll.get_data_by_id(3)
        assert user_data == {'id': 3, 'username': 'mosh_s'}
