from dataclasses import dataclass

@dataclass(order=True)
class Employee:
    name: str
    grade: int

employee1 = Employee(name="John", grade=5)
employee2 = Employee(name="John", grade=4)

print(employee1 > employee2)  # Output: True
