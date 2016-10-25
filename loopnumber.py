#I love number and always try to play with them
# Before going through this code, you sould watch this one
# https://www.youtube.com/watch?v=d8TRcZklX_Q

# I was trying to figure out what about the rest, like 5, 6, 7, 8 or n digits
#And, I have got something really intersting
#If you try, you will get amazed 


# Will count your given number
e = []

while True:
    print ('Write down a number 9 < n, if you want to continue the loop')
    n = int(input())
    
    if n == 0 <= 9:
        break
    else:
        #Will ascending number
        a = int(''.join(sorted(str(n))))

        #Will descending number
        b = int(''.join(sorted(str(n), reverse = True)))

        # Going to subtract descending to ascending
        c = b - a 
        e = e + [n]
        print (e)
        print ('New number = ' + str(c) + ', write down the new number')
final = len(e)
lastvalue = final - (final + 1)

print ('Complete list' + str(e))
print ('Your final decesion is '+ str(e[lastvalue]))
