import time
from collections import defaultdict, Counter

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# original solution

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# solution 1 ("naive"):
# default dict; we can use collections.defaultdict with lambda set to 0 and just increment the value instead.

# counts = dict()
# for elem in names_1:
#     if elem not in counts:
#         counts[elem] = 1
#         continue
#     counts[elem] += 1
# for elem in names_2:
#     if elem not in counts:
#         counts[elem] = 1
#         continue
#     counts[elem] += 1
# duplicates = [k for k, v in counts.items() if v > 1]

# solution 2 - defaultdict - a little bit slower overall:

# counts = defaultdict(lambda: 0)
# for elem in names_1:
#     counts[elem] += 1
# for elem in names_2:
#     counts[elem] += 1
# duplicates = [k for k, v in counts.items() if v > 1]

# solution 3 - sets intersection:
# duplicates = list(set(names_1) & set(names_2))

# stretch solution: O(n log n) time, O(n) space
names_2.sort()  # timsort, O(n log n)


# O(log n), but slow as we write python code. with implementation in C/C++ or fortran it'd be few times faster
def pseudolowerbound(arr, x):
    L = 0
    R = len(arr)
    m = -1
    while L < R:
        m = (L+R)//2
        if x <= arr[m]:
            R = m
        else:
            L = m + 1
    return arr[L] == x


duplicates = []

for elem in names_1:
    if pseudolowerbound(names_2, elem):
        duplicates.append(elem)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print(f"{len([k for k,v in counts.items() if v>1])} duplicates:\n\n{', '.join([k for k,v in counts.items() if v>1])}\n\n") if we have really tight memory
print(f"runtime: {end_time - start_time} seconds")
