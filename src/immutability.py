from dataclasses import dataclass

@dataclass(frozen=True)
class MyEmployee_immutable:
    name: str
    employee_id: int

employee = MyEmployee_immutable("John", 2)
# employee.name = "Joe"  # This will raise a FrozenInstanceError
print(employee)  
