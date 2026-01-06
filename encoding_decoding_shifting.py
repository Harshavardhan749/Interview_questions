# it is to endode and decode the string given by shifting the 
# characters in the alphabits 

instr=input("Enter the string")
shift=int(input("Enter number"))
#function for check number
def check(num):
    if num<26:
        return num
    else:
        num-=26
        check(num)

def decode(num):
    if num<26:
        return num
    else:
        num-=26
        decode(num)

result=[]
caps=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
small=list('abcdefghijklmnopqrstuvwxyz')
liststr=list(instr)
#encoding section
for i in liststr:
    if i in small:
        num=small.index(i)
        num+=shift
        l=check(num)
        result.append(small[l])
    elif i in caps:
        num=caps.index(i)
        num+=shift
        l=check(num)
        result.append(caps[l])
    else:
        result.append(i)
encodedstr=''.join(result)
print("encoding",encodedstr)
#decoding section
original=[]
for i in result:
    if i in small:
        num=small.index(i)
        num-=shift
        l=decode(num)
        original.append(small[l])
    elif i in caps:
        num=caps.index(i)
        num-=shift
        l=decode(num)
        original.append(caps[l])
    else:
        original.append(i)
decodedstr=''.join(original)
print("decode",decodedstr,"by the shift of ",shift)

#inputs : harsha, shift:2
#ouput :-encode : jctujc ,decode : harsha shift is 2
