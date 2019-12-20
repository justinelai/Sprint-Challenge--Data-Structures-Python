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
        
        if self.current is None:
            self.current = self.storage.head #initialize current at head.
        if self.storage.length == self.capacity: #if DLL is full
            self.current.value = item
            if self.current.next is not None:
                self.current = self.current.next
            else:
                self.current = self.storage.head
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # returns all of the elements in the buffer in a list in their given order
        # do not return None values in the list even if they are present:
        nextlist = self.storage.head
        while nextlist is not None:
            list_buffer_contents.append(nextlist.value)
            nextlist = nextlist.next
        
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
