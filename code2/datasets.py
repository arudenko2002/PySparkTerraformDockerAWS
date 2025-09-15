ar1 = [1,2,3,4,5]

ar2 = ar1[::-1]
print("reverse order", ar2)
# reverse order [5, 4, 3, 2, 1]

ar3 = ar1.pop()
print("popped value=", ar3)
# popped value: 5
print("without last element", ar1)
# without last element: [1, 2, 3, 4]

ar4 = ar1[:len(ar1)-1]
print("without last element 2:", ar4)
# without last element 2: [1, 2, 3]

ar1_2 = [1,2,3,4,5]
ar5 = ar1[::len(ar1_2)-1]
print("return to the first element: ",ar5)
# return to the first element:  [1]

str1 = "12345"
print("original",str1)
str2 = str1[::-1]
print("reversed",str2)
str3 = list(str1)
print("pop from list last element", str3)
str4 = str3.pop()
str5 = ''.join(str3)
print("str5=", str1, str4, str5)

str1="12345"
print("third element", str1)
print("every 1st in reverse order::-1=",str1[::-1]) #54321
print("every 2nd in reverse order::-2=",str1[::-2]) #531
print("every 3d  in reverse order::-3=",str1[::-3]) #52
print("every 4th in reverse order::-4=",str1[::-4]) #5
print("every 5th in reverse order::-5=",str1[::-5]) #5
print("every 6th in reverse order::-6=",str1[::-6]) #5
print("every 7th in reverse order::-7=",str1[::-7]) #5
print("every 8th in reverse order::-8=",str1[::-8]) #5

print("third element", str1) #[12345]
print("every 1st in straight order::1=",str1[::1]) #12345
print("every 2nd in straight order::2=",str1[::2]) #135
print("every 3d  in straight order::3=",str1[::3]) #14
print("every 4th in straight order::4=",str1[::4]) #15
print("every 5th in straight order::5=",str1[::5]) #1
print("every 6th in straight order::6=",str1[::6]) #1
print("every 7th in straight order::7=",str1[::7]) #1
print("every 8th in straight order::8=",str1[::8]) #1


ar1 = [1,2,3,4,5]
ar2 = [6,7,8,9,0]
ar1.extend(ar2)
print("ar1.extend(ar2)=",ar1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("ar1.extend(ar2)=",ar1+ar2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 6, 7, 8, 9, 0]
d1 = {"a":"1", "b":"2", "c":"3"}
d2 = {"d":"4", "e":"5", "f":"6"}
d1.update(d2)
print("d1.update(d2)=",d1) # {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': 6}

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set = set1.union(set2)
print("set1.union(set2)=", set)  # {1, 2, 3, 4, 5, 6, 7}
set = set1.intersection(set2)
print("set1.intersection(set2)=", set) # {3, 4, 5}
set = set1.update(set2)
print("update is same as union = ", set1)  # {1, 2, 3, 4, 5, 6, 7}
set = set1.difference(set2)
print("set1.difference(set2)=", set)
set = set2.difference(set1)
print("set1.difference(set1)=", set)

print("set1=",set1)
set1.pop()
print("set1.pop()=", set1)
set1.pop()
print("set1.pop()=", set1)
set1.add(8)
print("set1.add(8)=", set1)
set1.remove(8)
print("set1.remove(8)=",set1)
ar = [1,2,3,4,5]
set1 = list(ar)
set4 = set(list([3,4,5,6,7]))
