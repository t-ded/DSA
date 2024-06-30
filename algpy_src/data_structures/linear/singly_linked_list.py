from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Optional, TypeVar

from algpy_src.data_structures.data_structure import DataStructure

T = TypeVar("T")


@dataclass
class LinkedListNode:

    def __init__(self, value: T):
        self.index: int = 0
        self.value: T = value
        self.successor: Optional[LinkedListNode] = None

    def add_successor(self, value: T) -> None:
        successor = LinkedListNode(value)
        successor.index = self.index + 1
        self.successor = successor


class SinglyLinkedList(DataStructure):

    def __init__(self) -> None:
        super().__init__()
        self.head: Optional[LinkedListNode] = None
        self.length: int = 0

    @property
    def name(self) -> str:
        return 'Singly Linked List'

    @property
    def best_case_insert_time_complexity(self) -> str:
        return '1'

    @property
    def best_case_insert_description(self) -> str:
        return 'index 0'

    @property
    def average_case_insert_time_complexity(self) -> str:
        return 'n'

    @property
    def worst_case_insert_time_complexity(self) -> str:
        return 'n'

    @property
    def worst_case_insert_description(self) -> str:
        return 'index equals length'

    @property
    def best_case_delete_time_complexity(self) -> str:
        return '1'

    @property
    def best_case_delete_description(self) -> str:
        return 'item in head'

    @property
    def average_case_delete_time_complexity(self) -> str:
        return 'n'

    @property
    def worst_case_delete_time_complexity(self) -> str:
        return 'n'

    @property
    def worst_case_delete_description(self) -> str:
        return 'item at tail'

    @property
    def best_case_search_time_complexity(self) -> str:
        return '1'

    @property
    def best_case_search_description(self) -> str:
        return 'item in head'

    @property
    def average_case_search_time_complexity(self) -> str:
        return 'n'

    @property
    def worst_case_search_time_complexity(self) -> str:
        return 'n'

    @property
    def worst_case_search_description(self) -> str:
        return 'item not present'

    @property
    def space_complexity(self) -> str:
        return 'n'

    def insert(self, data: T, index: int) -> int:
        n_ops = 0
        if index > self.length:
            logging.warning('Index out of range.')
        else:
            if self.head is None:
                self.head = LinkedListNode(data)

            else:
                current = self.head
                for i in range(index - 1):
                    if current.successor is not None:
                        current = current.successor
                        n_ops += 1
                current.add_successor(data)
                self.length += 1
        return n_ops

    def delete(self, data: T, index: Optional[int]) -> int:
        n_ops = 0
        return n_ops

    def search(self, data: T) -> tuple[Optional[int], int]:
        n_ops = 0
        location = None
        return location, n_ops

    def print_time_complexity_info(self) -> None:
        """
        Print the time complexity information breakdown of Singly Linked List per insertion, deletion and search.
        """
        print(f'Time complexity breakdown of {self.name} data structure:')

        print(f'\tInsertion:')
        print(f'\t\tBest case time complexity is O({self.best_case_insert_time_complexity}) with best case being {self.best_case_insert_description}.')
        print(f'\t\tAverage case time complexity is O({self.average_case_insert_time_complexity}).')
        print(f'\t\tWorst case time complexity is O({self.worst_case_insert_time_complexity}) with worst case being {self.worst_case_insert_description}.')

        print(f'\tDeletion:')
        print(f'\t\tBest case time complexity is O({self.best_case_delete_time_complexity}) with best case being {self.best_case_delete_description}.')
        print(f'\t\tAverage case time complexity is O({self.average_case_delete_time_complexity}).')
        print(f'\t\tWorst case time complexity is O({self.worst_case_delete_time_complexity}) with worst case being {self.worst_case_delete_description}.')

        print(f'\tSearch:')
        print(f'\t\tBest case time complexity is O({self.best_case_search_time_complexity}) with best case being {self.best_case_search_description}.')
        print(f'\t\tAverage case time complexity is O({self.average_case_search_time_complexity}).')
        print(f'\t\tWorst case time complexity is O({self.worst_case_search_time_complexity}) with worst case being {self.worst_case_search_description}.')



