size=int(input('Enter size of the list :'))
lst=[]
for i in range(size):
    i=int(input("enter a number :"))
    lst.append(i)
print('original list :',lst)
square_lst=list(map(lambda num: (num)**2,lst))
print('result :',square_lst)