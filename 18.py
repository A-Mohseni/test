# s=0
# a=int(input('  ?  '))
# while a>=0:
#     s+=a
#     a=int(input('  ?  '))
# print(s)



# s=0
# while True:
#     a=int(input("   ?   "))
#     if a <=0:
#         break
#     s+=a
# print(s)    



# s=0
# while True:
#     a=int(input("   ?   "))
#     if a <=0:
#         break
#     if a % 3!=0:
#         s+=a
# print(s)    



s=0
while True:
    a=int(input("   ?   "))
    if a <=0:
        break
    if a % 3==0:
        continue
    s+=a
print(s)    