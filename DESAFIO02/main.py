from math import sqrt
def F(n):
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

def Fibonacci(num):
    result = False
    n = 0
    cur = F(n)
    while cur <= num:
        if num == cur:
            result = True
        n += 1
        cur = F(n)
    if result == True:
        print('O número ({}) informado faz parte da sequência de Fibonacci'.format(num))
    else:
        print("O número informado ({}) não faz parte da sequência de Fibonacci".format(num))

num = int(input("Informe um número: "))
print(type(num))

Fibonacci(num)