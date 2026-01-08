#it is to print arthimetic operation on the prime number 
#at the position m.

m=int(input("Enter the number"))
prime_list=[2,3]
i=3
while len(prime_list)<=(m+1):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
        else:
            if i not in prime_list:
                prime_list.append(i)
    i+=1
sum_num=(prime_list[m]%10+prime_list[m]//10)*prime_list[m]

print(sum_num)

#input:6
#6th prime is 13 ; 1+3=4; 4*13=52
#output:52
