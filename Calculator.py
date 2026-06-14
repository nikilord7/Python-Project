class Calculator:

    def Add(self, A, B):
        return A + B

    def Subtract(self, A, B):
        return A - B

    def Multiply(self, A, B):
        return A * B

    def Divide(self, A, B):
        if B == 0:
            raise ValueError("Delen door nul is niet toegestaan.")
        return A / B