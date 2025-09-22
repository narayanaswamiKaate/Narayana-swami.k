class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b == 0:
                return "Error: Division by zero is not allowed"
            return self.a / self.b
        else:
            return "Invalid operation"


# Example usage:
calc1 = Calculator(10.5, 5.5, "add")
print("Result:", calc1.calculate())

calc2 = Calculator(10.5, 0, "divide")
print("Result:", calc2.calculate())

calc3 = Calculator(7, 3, "multiply")
print("Result:", calc3.calculate())
