class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is None:
            self.head = Node(data, self.head)
            self.tail = self.head
        else:
            self.head = Node(data, self.head)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.head is None:
            self.head = Node(data, self.head)
            self.tail = self.head
        else:
            self.tail.next_node = Node(data, None)
            self.tail = self.tail.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        node = self.head
        if node is None:
            return None

        ll_list = []
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, id_to_find):
        node = self.head
        if node is None:
            return None
        while node:
            try:
                if node.data["id"] == id_to_find:
                    return node.data
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")
            node = node.next_node

