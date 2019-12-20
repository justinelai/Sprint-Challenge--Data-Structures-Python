from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # integer, fixed
        self.current = None # Index of oldest element... location where "current"/new element will be placed?
        self.storage = DoublyLinkedList()

    def append(self, item):
        # adds elements to the buffer - no APPEND method. reassignment?
        # oldest element in the ring buffer is overwritten with the newest element
        
        self.current = 0 #initialize empty DLL.
        
        if self.storage.length == self.capacity: #if DLL is full
            pass
        self.storage.add_to_tail(item)
        self.current += 1 # current must increase, but should be able to loop back to zero if it reaches capacity.


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # returns all of the elements in the buffer in a list in their given order (OLDEST VALUE FIRST? if so, not necessarily head or tail)
        # do not return None values in the list even if they are present
        for entry in range(self.storage.length):
           list_buffer_contents.append(entry)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
