import os
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def Suma(num1,num2):
    suma = num1 + num2
    print(f'{num1} + {num2} = {suma}')

def Resta(num1,num2):
    resta = num1 - num2

    print (f'{num1} - {num2} = {resta}' )

def Multiplicacion(num1,num2):

    multiplicaion = num1*num2
    print(f"{num1} * {num2} = {multiplicaion}")

def Division(num1,num2): 

    if num2 != 0:
        resultado=num1/num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Error: Can't divide by zero!!")       

def main():
    print("\n"+"-"*10 + "Welcome to the calculator" + "-"*10)
    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
          
    5. Exit""")

    print("\n"+"-"*45+"\n")

Cont = 0 
while Cont != 5:
    main()
    Cont = input("Enter your option: ")
    if Cont == "5":
        break
    try:
        num1 = float(input("Please, enter a number: "))
        num2 = float(input("Please, enter a number: "))
    except ValueError:
        # Código que se ejecuta si ocurre el error específico
        print("¡Error! You can't enter that value!")
    else:
        if Cont == "1":
            limpiar_pantalla()
            Suma(num1,num2)    
        elif Cont == "2":
            limpiar_pantalla()
            Resta(num1,num2)
        elif Cont == "3":
            limpiar_pantalla()
            Multiplicacion(num1,num2)
        elif Cont == "4":
            limpiar_pantalla()
            Division(num1,num2)
        else:
            print("ERROR!¡!¡!¡!¡")