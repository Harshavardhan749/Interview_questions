#it is take an array of numbers and a "k"th value as inputs.
# it results array which cointains all "k"th values at last with non character 
# present in the array.


l1=eval(input("Enter the numbers"))
k=int(input("Enter choosen letter"))
count=0
leng=len(l1)
l1=[i for i in range(leng) if l1[i] !=k ]  # to remove all k values from the list
count=leng-len(l1)
for i in range(count):
    l1.append('_')
print(l1,count)

#sample input array=[3,2,2,3] ,k=3
#ouput [2,2,_,_]
