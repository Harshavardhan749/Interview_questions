#it is a simple program to swap case of a string
#it uses the ord() function to get the ASCII value of a character and then checks if it is upper or lower case.
#if it is upper case it converts to lower case and vice versa.
#by chr() function it converts the ASCII value back to character.

string=list(input("Enter string:")) # LEARN_PYHTON@1234
for i in string:
    j=ord(i)
    if j>=65 and j<=90:
        j+=32
        print(chr(j),end='')
    elif j>=97 and j<=122:
        j-=32
        print(chr(j),end='')
    else:
        print(chr(j),end='')

"""
output:-
Enter string: LEARN_PYHTON@1234
output is : learn_python@1234
"""
