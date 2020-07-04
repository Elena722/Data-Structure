 class Box:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        prev_str = "<->" if self.prev else ""
        # prev_str = str(self.prev) if self.prev else ""
        next_str = str(self.next) if self.next else ""
        return f"{prev_str} {self.value} {next_str}"

class LinkedList:
    def __init__(self):
        self.head = None

    def get_last_element(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            prev = current
            current = current.next
        return prev

    def add_to_end(self, value):
        obj = Box(value)
        if self.head is None:
            self.head = obj
            return
        current = self.get_last_element()
        current.next = obj
        obj.prev = current

    def get_second_to_last(self):
        if self.head is None:
            return
        current = self.get_last_element()
        if current is None:
            return
        print(current.prev)
        return current.prev

    def add_to_beggining(self, value):
        obj = Box(value)
        if self.head is None:
            self.head = obj
            return
        current = self.head
        while current is not None:
            prev = current
            current = current.prev
        current = prev
        current.prev = obj
        obj.next = current

    def __contains__(self, item):
        if self.head is None:
            return
        current = self.head
        if current.value == item:
            return True
        while current is not None:
            if current.value == item:
                return True
            current = current.next
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            current = current.prev

    def __len__(self):
        if self.head is None:
            return
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        current = self.head
        while current.prev is not None:
            count += 1
            current = current.prev
        return count

    def get_first(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            prev = current
            current = current.prev
        current = None
        return prev

    def extend(self, second):
        second = second.get_first()
        first = self.get_last_element()
        if second is None and first is None:
            return
        elif second is None:
            return first
        elif first is None:
            return second
        second.prev = first
        first.next = second


    def print(self):
        if self.head.prev is None:
            print(str(self.head))
            return
        current = self.head
        while current.prev is not None:
            current = current.prev
        print(str(current))

o = LinkedList()
o.add_to_end(5)
o.add_to_end(6)
o.add_to_end(7)
o.add_to_end(8)
o.add_to_end(9)
o.print()
print(o.get_last_element())
print(o.get_second_to_last())
o.add_to_beggining(4)
o.print()
o.add_to_beggining(3)
o.print()
print(9 in o)
print(10 in o)
print(3 in o)
print(2 in o)
print(len(o))
print(o.get_first())   # 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8 <-> 9
e = LinkedList()
e.add_to_end(10)
e.add_to_end(11)
e.add_to_end(12)
e.print()  # 10 <-> 11 <-> 12
o.extend(e)
o.print()  #  3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8 <-> 9 <-> 10 <-> 11 <-> 12