# myList = ["apple", "dog", 5, True]
# myList2 = list()         # []

# item = myList[0]         # index must be less than n
# item2 = myList[-1]       # last item, -2 for second last item

# # for x in myList:
# # 	print(x)

# # if "dog" in myList:
# # 	print("yes")
	
# n = len(myList)

# myList.append("lemon")
# myList.insert(1, "banana")   # insert banana at index 1
# lastElement = myList.pop()   # .pop() returns the last item and also removes it
# myList.remove("apple")      # to remove an element by value, if its not present you will get a ValueError, so be careful
# # myList.clear()              # remove all elements
# myList.reverse()            # reverses in place

# myList = [3, 5, 1, 6, 2]
# # myList.sort()               # in place
# newList = sorted(myList)        # doesn't change the original list

# list3 = [0] * 5                # fast way to initialize lists

# myList2 = myList + list3        # easily concatenate two lists

# print(myList2)

# # slicing: an easy way to access subarray of your list

myList = [x for x in range(10)]     # myList is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# slicedList = myList[1:5]            # [1, 2, 3, 4], start index 1 to stop index 5, index 5 is excluded
# slicedList = myList[:5]             # [0, 1, 2, 3, 4], start from the beginning
# slicedList = myList[1:]             # [1, 2, 3, 4, 5, 6, 7, 8, 9], start from 1 go till the end
# slicedList = myList[:]              # entire list  
# slicedList = myList[::2]            # [0, 2, 4, 6, 8], step index, every second item, start with first, basically i=0;i<n;i+=2
# slicedList = myList[::-1]           # nice way to reverse a list

# copying a list