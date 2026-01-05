# it takes a number input and takes that number of input string
# after it calculates how many distint strings are present in it
# and 2nd line shows that  how many time string1 , string n repeats

string=[]
number=int(input("Enter number"))
count_number=number
sub_string=[]
for i in range(number):
    strings=input('>>>')
    string.append(strings)
string_set=set(string)
for i in string_set:
    j =string.count(i)
    if j>=2:
        count_number-=1
        print(count_number)
for i in string:
    if i not in sub_string:
        sub_string.append(i)

for i in sub_string:
    number2=string.count(i)
    print(number2  ,end=' ')

'''
sample o/p:-
Enter number4
>>>bcdef
>>>adcdefg
>>>bcde
>>>bcdef
3
2 1 1'''
