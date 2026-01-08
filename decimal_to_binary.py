#to convert the given number to binary number

input_number=int(input("Enter the number"))
original_number=input_number
if input_number<0:
    print("invalid")
reminder=0
result=[]
while input_number!=0:
    

    reminder=input_number%2
    input_number//=2

    result.append(reminder)

j="".join(map(str,result))
print(f"binary of {input_number}the digit is",j[::-1])

#output:binary of 22 the digit is 10110
