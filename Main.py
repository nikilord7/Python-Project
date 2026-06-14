#Import necessary classes
from Calculator import Calculator
from History import HistoryManager

#Create instances of the classes
calculator = Calculator()
history = HistoryManager()

#The main loop for options
while True:
    
    #Different menu options
    print("\n=== CALCULATOR ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Clear History")
    print("7. Exit")
    
    #User input for a menu choice
    Choice = input("Make a choice: ")
    
    #Close application option
    if Choice == "7":
        print("Application closed.")
        break
    
    #View history option
    elif Choice == "5":

        Calculations = history.LoadHistory()

        if not Calculations:
            print("No history found.")
        else:
            for item in Calculations:
                print(item)
    
    #Clear history option
    elif Choice == "6":

        history.ClearHistory()
        print("History cleared.")
    
    #Perform calculations based on user choice
    elif Choice in ["1", "2", "3", "4"]:

        try:
            A = float(input("First number: "))
            B = float(input("Second number: "))

            #Additions
            if Choice == "1":
                Result = calculator.Add(A, B)
                Text = f"{A} + {B} = {Result}"
            
            #Subtractions
            elif Choice == "2":
                Result = calculator.Subtract(A, B)
                Text = f"{A} - {B} = {Result}"

            #Multiplications
            elif Choice == "3":
                Result = calculator.Multiply(A, B)
                Text = f"{A} * {B} = {Result}"

            #Divisions
            elif Choice == "4":
                Result = calculator.Divide(A, B)
                Text = f"{A} / {B} = {Result}"
                
            #Display result
            print("Results:", Result)
            
            #Save calculation to history
            history.SaveCalculation(Text)
        
        #Error handling
        except ValueError as Error:
            print("Error:", Error)

    else:
        print("Invalid choice.")