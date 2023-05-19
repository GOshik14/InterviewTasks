import time


def simple_iintegers(end: int) -> list:
    answ = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 39, 41, 43, 47, 53]

    if end > 54:
        for i in range(53, end+1, 2):
            simple_flag = True
            for j in range(3, i, 2):
                if i % j != 0:
                    simple_flag = False
                    break
            if simple_flag:
                answ.append(i)

    return answ

def simple_integers_included(n: int) -> list:
    if n == 1:
        return [1]
    simple_d = simple_iintegers(n-1)
    answ = []
    flag_end = False
    for d in simple_d:
        if not flag_end:
            os = n % d
            while os == 0:
                answ.append(d)
                n = n // d
                if n in simple_d:
                    answ.append(n)
                    flag_end = True
                    break
                os = n % d
    return answ


integer_digit = int(input("Enter digit for perfoming: "))
# print(*simple_integers_included(integer_digit))
for i in range(1, integer_digit+1):
    print(*simple_integers_included(i))
    time.sleep(1)
