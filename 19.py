from random import randint
n=randint(1,100)
c=0
while c < 7 :
    c+=1
    a=int(input('   ?   '))
    if a==n:
        print('you won')
        exit()
    elif n > a:
        print("greater")
    elif n < a:
        print('smaller')
print("you lost")        