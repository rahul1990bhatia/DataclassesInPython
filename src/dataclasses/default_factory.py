from dataclasses import dataclass, field
from typing import List

@dataclass
class MyEmployee:

    name: str
    employee_id: int
    location: str
    skills: list
    is_contractor: bool = False
    projects: List[str] = field(default_factory=list)

if __name__ == '__main__':
    employee1 = MyEmployee(name='John', employee_id=1, location='Paris', skills=['Python'])
    employee2 = MyEmployee(name='Joe', employee_id=2, location='London', skills=['ProjectManager'], is_contractor=True)
    employee3 = MyEmployee(name='Joe', employee_id=2, location='London', skills=['ProjectManager'], projects=['Alpha', 'Beta'])
    print(employee1)
    print(employee2)
    print(employee3)