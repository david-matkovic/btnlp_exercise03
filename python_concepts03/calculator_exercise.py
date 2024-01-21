class Calculator:
    def __init__(self):
        pass

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def division(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

    def multiplication(self, a, b):
        return a * b

class Special(Calculator):
    def modulo(self, a, b):
        return a % b

    def exponential(self, a, b):
        return a ** b


calc = Special()
print(calc.addition(10, 5))      
print(calc.subtraction(10, 5))   
print(calc.multiplication(10, 5))
print(calc.division(10, 5))      
print(calc.modulo(10, 5))        
print(calc.exponential(10, 5))   
