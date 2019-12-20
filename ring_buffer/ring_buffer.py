from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # integer, fixed
        self.current = None # Quasi index of oldest element... location where "current"/new element will be placed? but only for a linked list.
        self.storage = DoublyLinkedList()

    def append(self, item):
        # adds elements to the buffer - no APPEND method. reassignment? FIFO
        # oldest element in the ring buffer is overwritten with the newest element
        # instead, oldest element is head
        self.current = self.storage.head
        if self.storage.length == self.capacity: #if DLL is full
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.current.next
            # self.current += 1 % self.capacity # current must increase, but should be able to loop back to zero if it reaches capacity. Modulo.
        else:
            self.storage.add_to_tail(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # returns all of the elements in the buffer in a list in their given order (OLDEST VALUE FIRST? if so, not necessarily head or tail)
        # do not return None values in the list even if they are present:
        while self.current is not None:
            list_buffer_contents.append(self.current.value)
            self.current = self.current.next
        
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
