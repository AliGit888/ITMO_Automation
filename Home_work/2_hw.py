def task_1():
    a: int = 1
    b: float = 2.5
    c: str = 'cat'
    d: list = [3,4]
    e: bool = True
    return a,type(a),b,type(b),c,type(c),d,type(d),e,type(e)
print (task_1())


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]
print(task_2())


def task_3(a: int) -> int:
    return a*a
print (task_3(25))