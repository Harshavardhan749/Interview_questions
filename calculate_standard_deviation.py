#to find mean and standard deviation of the given numbers

import math
numbers=[5,0,2,4,4,4,5]
means=[]
n=len(numbers)
sum_observations=sum(numbers)
mean=sum_observations/n
for i in numbers:
    k=round((i-mean)**2,2)
    means.append(k)
sum_means=sum(means)
sd=(round(math.sqrt((sum_means/n)),2))
print(sd)

#output:1.68
