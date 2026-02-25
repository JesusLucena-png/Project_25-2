def main():
    print("-"*10 + "Welcome to the calculator" + "-"*10)
    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
          
    5. Exit""")

    print("-"*45)

Cont = 0 
while Cont != 5:
    main()
    Cont = int(input("Enter your option: "))
    if Cont == 1:
        Sum()    
    elif Cont == 2:
        Rest()
    elif Cont == 3:
        Mul()
    elif Cont == 4:
        Div()
    elif Cont == 5:
        break
    else:
        print("!¡!¡!¡!¡ERROR!¡!¡!¡!¡")
    
