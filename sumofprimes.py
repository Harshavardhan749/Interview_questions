#it is to print the sequence of prime numbers and returns
#the sum of m to n prime numbers in the series

prime_list=[2]
m=int(input("Enter the first number"))
n=int(input("Enter the second number"))
i=3
while len(prime_list)<=(m+n):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
        else:
            if i not in prime_list:
                prime_list.append(i)
    i+=1
print(sum(prime_list[m-1:m+n]))


#input:6,2
# 13+15+17=45 
#output:45
