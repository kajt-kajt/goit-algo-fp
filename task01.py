"""
Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

    написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
    розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
    написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

- Реалізовано функцію реверсування однозв'язного списку, яка змінює посилання між вузлами. Код виконується.
- Програмно реалізовано алгоритм сортування (функцію) для однозв'язного списку. Код виконується.
- Реалізовано функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список. Код виконується.
    
"""

class Node:
    """
    Class represents node of linked list
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """
    Class represents linked list data structure
    """
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        current = self.head
        new_tail = None
        while current:
            old_link = current.next
            current.next = new_tail
            new_tail = current
            current = old_link
        self.head = new_tail

    def bubble_sort_list(self):
        """
        Bubble sort is the easiest sorting algorithm to implement for linked lists 
        as it operates with neighbor nodes only
        """
        if not self.head or not self.head.next:
            return self.head
        changes_present = True
        while changes_present:
            changes_present = False
            prev_current = None
            current = self.head
            current2 = self.head.next
            while current and current2:
                if current.data > current2.data:
                    # lets change their order
                    if current == self.head:
                        self.head = current2
                    tail = current2.next
                    if prev_current:
                        prev_current.next = current2
                    prev_current = current2
                    current.next = tail
                    current2.next = current
                    current2 = current.next 
                    changes_present = True  
                else:
                    prev_current = current
                    current = current2
                    current2 = current2.next
                #print("="*20)
                #self.print_list()
                #print("="*20)
    
def merge_sorted_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    """
    Merges 2 sorted lists into single sorted one
    """
    result = LinkedList()
    # let's insert new items to the beginning and than reverse all the list
    # should be much better for performance comparatively to inserting to the end of list
    l1_head = l1.head
    l2_head = l2.head
    while l1_head and l2_head:
        if l1_head.data < l2_head.data:
            result.insert_at_beginning(l1_head.data)
            l1_head = l1_head.next
        else:
            result.insert_at_beginning(l2_head.data)
            l2_head = l2_head.next
    while l1_head:
        result.insert_at_beginning(l1_head.data)
        l1_head = l1_head.next
    while l2_head:
        result.insert_at_beginning(l2_head.data)
        l2_head = l2_head.next
    result.reverse_list()
    return result

# ll1 = LinkedList()
# ll1.insert_at_beginning(2)
# ll1.insert_at_beginning(8)
# ll1.insert_at_beginning(10)
# ll1.insert_at_beginning(1)
# ll1.bubble_sort_list()
# 
# ll2 = LinkedList()
# ll2.insert_at_beginning(22)
# ll2.insert_at_beginning(8)
# ll2.insert_at_beginning(1)
# ll2.insert_at_beginning(15)
# ll2.bubble_sort_list()
# 
# ll3 = merge_sorted_lists(ll1,ll2)
# 
# ll1.print_list()
# print("-"*20)
# ll2.print_list()
# print("-"*20)
# ll3.print_list()
# print("-"*20)
# ll3.reverse_list()
# ll3.print_list()

