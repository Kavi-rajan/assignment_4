size=int(input('Enter size of the list :'))
lst=[]
for i in range(size):
    i=int(input("enter a number :"))
    lst.append(i)
print('original list :',lst)
tripled_lst=list(map(lambda num: (3*num),lst))
print('result :',tripled_lst)
