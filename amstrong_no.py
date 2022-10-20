# This program is used for finding the amstrong numbers

# The short describtion is about this code is,

n=int(input())
for j in range(n+1):
    num=j
    result=0
    while i!=0:
        digit=i%10            # take the last value of the input
        result=result+digit**len(str(i))    # the power of digit with respect to the input value
        i=i//10   # Then the identified value is take out from the string
if num==result:                
    print("yes,it's an amstrong number")
else:
    print("no,it's not an amstrong number")


#Finally check the value is equal to the given input

