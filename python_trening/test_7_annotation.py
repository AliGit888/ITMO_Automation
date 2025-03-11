a: int=5 # int - аннотация типа
b: str= 'строка'
c: list= [1,2]

def ident(s:str, width:int) -> str: #ключ слово def, аргументы str и int,возвращаемое число указывается после стрелки и до завершающего двоеточия
    return " " * (max(0,width-len(s)))+s
print (ident('123',69 ))

