from dataclasses import dataclass, field

@dataclass(frozen=True)
class MyEmployee_immutable:
    name: str
    employee_id: int
    year_of_joining: int = field(default = 2020, compare=False)

employee1 = MyEmployee_immutable("John", 1)
employee2 = MyEmployee_immutable("John", 1, 2021) 
print(employee1)  
print(employee2)  
print(employee1 == employee2)  
