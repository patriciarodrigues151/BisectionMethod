import math

def f(x):
    return math.sqrt(x) - 1.1
    
def bisection(a, b, atol):
    ite = 0
    while True:
        ite += 1
        print("iteração ",ite)
        c = (a + b) / 2
        print("a: ", a)
        print("b: ", b)
        print("c = (a+b)/2 = ", c)

        mult = f(a) * f(c)
        if mult > 0:
            a = c
            print("f(a).f(c) = f(", a, ").f(", c, ") = ",mult, " > 0")
            print("Logo, a = c = ", a)
        else:
            b = c
            print("f(a).f(c) = f(", a, ").f(", c, ") = ",mult, " < 0")
            print("Logo, b = c = ", b)
        if abs(f(c)) < atol or ite > 100:
            print("Como abs(f(c)) = ", abs(f(c)), "(criterio de parada)")
            break
    return c

def main():
    a = float(input("Digite a: "))
    b = float(input("Digite b: "))
    atol = float(input("Digite atol: "))
    if f(a) * f(b) > 0:
        print("Não há raiz no intervalo [", a, ",", b, "]")
    else:
        root = bisection(a, b, atol)
        print("A raiz encontrada foi", root)

main()
