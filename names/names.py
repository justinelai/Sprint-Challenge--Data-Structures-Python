import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
"""
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
"""

names_1.sort()
names_2.sort()

duplicates = []

j = 0
k = 0

while j <= 9999 and k <= 9999:
    if names_1[j] == names_2[k]:
        duplicates.append(names_1[j])
        j += 1
        k += 1
    elif names_1[j] < names_2[k]:
        j += 1
    else:
        k += 1
    


# ------- Student Response ----------
# Runtime on my machine was actually around 9-10 seconds! Ouch.
# The runtime complexity is O(n^2).
# I reduced it to 0.021649837493896484 seconds.
# 64 duplicates.
# -----------------------------------

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")




# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
