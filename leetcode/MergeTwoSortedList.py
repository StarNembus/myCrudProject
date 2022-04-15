"""Вам даны главы двух отсортированных связанных списков list1 и list2.

Объедините два списка в один отсортированный список. Список должен быть составлен путем соединения узлов первых двух списков.

Возвращает заголовок объединенного связанного списка """
from typing import Optional

"""Ввод: list1 = [1,2,4], list2 = [1,3,4]
 Вывод: [1,1,2,3,4,4]"""

""" C ListNode"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # dummy node to hold the head of the merged list
        # dummy узел для хранения заголовка объединенного списка
        dummy = ListNode()
        current = dummy
        while list1 or list2:
            # if list2 is None, then list1 is the next node
            # если list2 - None, тогда list1 является следующим узлом
            if list1 and not list2:
                next_value = list1.val
                list1 = list1.next
            # if list1 is None, then list2 is the next node
            # если list1 - None, тогда list2 является следующим узлом
            elif list2 and not list1:
                next_value = list2.val
                list2 = list2.next
            # if both list1 and list2 are not None, then compare the values
            # если и list1, и list2 не равны None, тогда сравните значения
            else:
                if list1.val <= list2.val:
                    next_value = list1.val
                    list1 = list1.next
                else:
                    next_value = list2.val
                    list2 = list2.next
            # set the next node and move to the next node
            # установить следующий узел и перейти к следующему узлу
            current.next = ListNode(next_value)
            current = current.next

        # return the head of the merged list
        # вернуть заголовок объединенного списка
        return dummy.next


# def mergeTwoLists(list1, list2):
#     my_list = []
#     i = 0
#     j = 0
#
#     while i < len(list1) and j < len(list2):
#         if list1[i] == list2[j]:
#             my_list.append(list1[i])
#             my_list.append(list2[j])
#             i = i + 1
#             j = j + 1
#         elif list1[i] > list2[j]:
#             my_list.append(list2[j])
#             j = j + 1
#         elif list1[i] < list2[j]:
#             my_list.append(list1[i])
#             i = i + 1
#
#     if i < len(list1):
#         my_list.extend(list1[i:])
#     elif j < len(list2):
#         my_list.extend(list2[j:])
#
#     return my_list
#
#
#
#
# list1 = [1, 2, 4]
# list2 = []
# print(mergeTwoLists(list1, list2))
