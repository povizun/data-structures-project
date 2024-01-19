class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
        else:
            new_tail = Node(data, None)
            self.tail.next_node = new_tail
            self.tail = new_tail

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is not None:
            old_head_data = self.head.data
            self.head = self.head.next_node
            return old_head_data
        else:
            return self.head

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        data = self.head
        to_return = []
        while data is not None:
            to_return.append(data.data)
            data = data.next_node
        return "\n".join(to_return)
