# it is to print the a list of numbers that are multiple of 
#numbers with in the input array . the values that are not multipled 
#at the same index.


arr=list(int(input("enter")))  #[1,2,3,4]
#arr=[1,2,3,4]
multiply=1
arr2=[]
for i in range(len(arr)):
    for j in range(len(arr)):
        if(i==j):
            continue
        else:
            multiply*=arr[j]
    arr2.append(multiply)
    multiply=1
print(arr2)

'''
input:-[1, 2, 3, 4]
output:-[24, 12, 8, 6]
'''
