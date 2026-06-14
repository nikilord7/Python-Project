#Calculator class to perform basic functions
class Calculator:
    
    #Addition function
    def Add(self, A, B):
        return A + B
    
    #Subtraction function
    def Subtract(self, A, B):
        return A - B

    #Multiplication function
    def Multiply(self, A, B):
        return A * B

    #Division function
    def Divide(self, A, B):
        if B == 0:
            raise ValueError("Delen door nul is niet toegestaan.")
        return A / B