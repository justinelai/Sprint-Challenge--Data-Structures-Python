import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

"""duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)"""

bst_1 = BinarySearchTree("")
for name_1 in names_1: 
    bst_1.insert(name_1)

bst_2 = BinarySearchTree("")
for name_2 in names_2: 
    bst_2.insert(name_2)



# ------- Student Response ----------
# Runtime on my machine was actually 9.307297706604004 seconds! Ouch.
# The runtime complexity is O(n^2).
# 


# -----------------------------------

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")




# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
