# it is to calculate no.of repeated ones and place in before  the repeated characters 

string_input=input("enter string:")
string_set=set(string_input)  
for i in string_set:
    number=string_input.count(i)
    print(f"output: {number}{i}",end=' ')
"""
output:-
enter string: harsha
output: 1r 1s 2a 2h
"""
