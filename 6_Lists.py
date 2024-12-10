list1 = ["A", "B", "C", "D"]
print(list1)
print(type(list1))

list2 = ["Bikram", 22, 94.6, ["A", "B", "C", "D"], (1, 2, 3), True, "E", "F"]
print(list2)
print(type(list2))

print(list2[0])
print(list2[-1])
print(list2[3][0])

list1[0] = "X"
print(list1)

del list1[0]
print(list1)

list1.insert(0, "A")
print(list1)

del list1[0]
print(list1)

list1 = ["A"] + list1
print(list1)

list1.append("E")
print(list1)

print(max(list1))
print(min(list1))

print(list1.index("C"))
print(list1[list1.index("C")])

list1.reverse()
print(list1)

list1 = list1[ : : -1]
print(list1)

print(list1.count("A"))
list1.append("A")
print(list1)
print(list1.count("A"))

list1.pop()
print(list1)

list3 = ["F", "G", "H", "I", "J", "K"]
print(list3)

list1.extend(list3)
print(list1)

list1.clear()
print(list1)

list4 = [8, 12, 5, 6, 17, 2]
print(list4)

list4.sort()
print(list4)

list4.sort(reverse=True)
print(list4)

list5 = list4
print(list4)
print(list5)

list5[2] = "X"
print(list5)
print(list4)

list6 = list4.copy()
print(list4)
print(list6)

list4[3] = "Y"
print(list4)
print(list6)

list7 = ["1", "2", "3"]
print(list7)

list8 = list(map(float, list7))
print(list8)

