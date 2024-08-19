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

@dataclass
class MyEmployee_Manager(MyEmployee):

    team_members: List[str] = field(default_factory=list)
    

if __name__ == '__main__':
    manager = MyEmployee_Manager(name='Jade', employee_id=2, location='London', skills=['ProjectManager'], projects=['Alpha', 'Beta'], team_members=['John', 'Joe'])
    print(manager) # MyEmployee_Manager(name='Jade', employee_id=2, location='London', skills=['ProjectManager'], is_contractor=False, projects=['Alpha', 'Beta'], team_members=['John', 'Joe'])

    