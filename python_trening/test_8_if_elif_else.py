num = 100
if num >=0:
    print ('число больше либо равно 0')
else:
    print('число отрицательное')

def task_yes_no(str_1,str_2):
    if str_1 in str_2:
        print ('да')
    else:
        print('нет')
task_yes_no(str_1='test', str_2='test1')

num_float=4.5
if num_float>0:
    print ('Положительное число')
elif num_float==0:
    print ('Ноль')
else:
    print('Чило отрицательно')

permit_print = True
num=-3
if num>0 and permit_print:
    print('num - положительное число')
elif not permit_print or num <0:
    print('Печать запрещена')

def kurs(year_of_study):
    if year_of_study == 1 or year_of_study ==2 or year_of_study == 3 or year_of_study == 4:
        print ('бакалавр')
    elif year_of_study in range (5,7):
        print ('магистр')
    elif 7 <= year_of_study <=9:
        print ('аспирант')
    else:
        print('Введите корректный год обучения')
kurs (9)

num = 99
if num>100 or num<-100:
    print ('-')
else:
    print ('+')