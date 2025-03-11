def task_2(num1,num2):
    if num1>num2:
        print (num1)
    elif num1<num2:
        print(num2)
task_2(num1 = 26,num2 =46)


def task_3(num3,num4):
    if num3-num4>=135 or num4-num3>=135:
        print ('Yes')
    else:
        print ('No')
task_3(num3=38,num4=30)


def task_4_months (seasons):
    if seasons ==12 or seasons ==1 or seasons ==2:
        print('winter')
    elif seasons in range (3,6):
        print('spring')
    elif seasons in range (6,9):
        print('summer')
    elif seasons in range (9,12):
        print('autumn')
task_4_months(9)


def task_5 (n1,n2,n3):
    if n1>10 and n2>10 and n3>10:
        print('Yes')
    else:
        print('No')
task_5(n1=11,n2=2,n3=20)
