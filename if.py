# n=int(input('enter a number'))
# if  n < 10 :
#     print('this is a one digital number')
# else:
#     print("this is a great number")   
# 
#  
# n=int(input('enter a number'))
# if n % 10 == 0:
#     print("eval")
# else:
#     print("odd")    



# n=int(input('enter a number'))
# if  n == 0 :
#     print("shanbe")
# if  n ==  1 :
#     print("ek shanbe")
# if  n ==  2 :    
#     print("do shanbe")
# if  n ==  3 :
#     print("se shanbe")
# if  n ==  4 :
#     print("char shanbe")
# if  n ==  5 :
#     print("pan shanbe") 
# if  n ==  6 :
#     print("jome")
# else:
#     print("wrong")

x=int(input("enter a number: "))
c = (x - 1) % 7 + 1
if c == 1:
    print("do_shanbe")
if c==2:
    print("se_shanbe")
if c==3:
    print("char_shanbe")
if c==4:
    print("panj_shanbe")
if c==5:
    print("jome")
if c==6:    
    print("shanbe")
if c==7:    
    print("yek_shanbe")
   