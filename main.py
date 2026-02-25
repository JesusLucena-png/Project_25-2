import division
import multiplation
import resta
import suma

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
    if Cont == "1":
        suma.Sum()    
    elif Cont == "2":
        resta.Rest()
    elif Cont == "3":
        multiplation.Mul()
    elif Cont == "4":
        division.Div()
    elif Cont == "5":
        break
    else:
        print("!¡!¡!¡!¡ERROR!¡!¡!¡!¡")
    
