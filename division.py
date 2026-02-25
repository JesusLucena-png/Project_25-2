def Div(): 
    num1=float(input("ingresa el dividendo: "))
    num2=float(input("ingresa el divisor: "))
    if num2 != 0:
        resultado=num1/num2
        print(f"el resultado de la division es {resultado}")
    else:
        print("error; no se puede dividir por cero")       