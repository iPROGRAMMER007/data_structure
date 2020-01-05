from array import *

arr = array('i',[])

n = int(input("Enter length of array: "))

k = 0

for  i in range(n):
    k = k+1
    print("Enter",k,"th","element: ",end="")
    element = int(input())
    arr.append(element)
print(arr)
print("Array lenght:",len(arr))


print("Enter number to search: ",end= "")
number = int(input())

k=0
for e in arr:
    if e==number:
        print("Search is successful element at",k)
        break
 #   else:
  #      print("Search is unsuccessful")

    k+=1

