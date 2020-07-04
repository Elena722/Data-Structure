class Box:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None

    def __str__(self):
        next_str = str(self.next) if self.next else ""
        return f"{self.value} - {next_str}"

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, new_value):
        obj = Box(new_value)
        if self.head is None:
            self.head = obj
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = obj

    def remove(self, remove_value):
        current = self.head
        if current is not None:
            if current.value == remove_value:
                self.head = current.next
                current = None
                return
            while current is not None:
                if current.value == remove_value:
                    break
                prev = current
                current = current.next
            if current is None:
                return
            prev.next = current.next
            current = None

    def contains(self, value):
        if self.head is None:
            return None
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __len__(self):
        if self.head is None:
            return None
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count += 1
        return count

    def get_element_by_index(self, index):
        if self.head is None:
            return None
        current = self.head
        number = 0
        while current is not None:
            if number == index:
                return current.value
            current = current.next
            number += 1
        return False

    def get_last_element(self):
        if self.head is None:
            return None
        current = self.head
        while current.next is not None:
            current = current.next
        # return current.value
        return current

    def get_second_to_last(self):
        if self.head is None:
            return None
        last = self.get_last_element()
        length = len(self)
        if length == 1:
            return None
        current = self.head
        while current.value != last.value:
            before_last = current
            current = current.next
        return before_last

    def get_first_element(self):
        if self.head is None:
            return None
        # return self.head.value
        return self.head

    def get_obj(self):
        return self.head

    def extend(self, second):
        first_list = self.get_last_element()
        second_list = second.get_first_element()  # full obj
        if first_list is None and second_list is None:
            return None
        elif first_list is None:
            return second_list
        elif second_list is None:
            return first_list
        first_list.next = second_list
        return first_list

    def print(self):
        print(str(self.head))

o = LinkedList()
o.add('first')
o.add('second')
o.add('third')
o.add('fourth')
o.add('fifth')
# we have a linked list with 5 items
# (first, (second, (third, (fourth, (fifth))))); (value, next)
print(o.contains('third'))  # True
o.remove('third')
print(o.contains('third'))  # False
print(o.get_element_by_index(2))  # fourth
print(o.get_element_by_index(10))  # False
print(o.get_last_element().value)  # fifth
print(o.get_second_to_last().value)  # fourth
print(len(o))  # 4
print(o.get_first_element().value)  # first

o.print()
print('---')

e = LinkedList()
print(e.get_element_by_index(2))  # None
e.add(0)
print(e.get_last_element().value)  # 0
print(e.get_second_to_last())  # None
e.print()
print('=====')
l = LinkedList()
l.add('last')
print(l.get_last_element().value)
l.extend(o)  # last
print(l.get_last_element().value)  # fifth
l.print()
