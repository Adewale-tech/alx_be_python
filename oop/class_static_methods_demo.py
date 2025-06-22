class Calculator:
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    # Static Method
    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    # Class Method
    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers after printing calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
