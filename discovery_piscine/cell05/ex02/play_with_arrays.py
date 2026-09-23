#!/usr/bin/env python3

arr1 =  [2, 8, 9, 48, 8, 22, -12, 2]
arr2 = []
arr3 = []
for i in arr1:
    arr2.append(i + 2)
for k in arr2:
    if k > 5:
        arr3.append(k)
print(arr1)
print(arr3)
