
def calc(a,b, oper):
    if oper == "+":
        soma = a + b 
        return soma
    elif oper == "-":
        subt = a - b
        return subt
    elif oper == "*":
        mult = a * b
        return mult
    elif oper == "/":
        div = a / b
        return 
    else:
        return "Vc digitou um operador inválido que precisa rever!"

num1 = int(input("Digite um valor: "))
num2 = int(input("Digite um valor: "))
operador = input("Digite um operador: ")
print(calc(num1, num2, operador))


