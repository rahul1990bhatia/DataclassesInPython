from dataclasses import dataclass

@dataclass
class MyEmployee:

    name: str
    employee_id: int
    location: str

class MyEmployee_old:

    def __init__(self, name, employee_id, location) -> None:
        self.name =  name
        self.employee_id = employee_id
        self.location = location

    def __repr__(self):
        return f"MyEmployee_old(name={self.name}, employee_id={self.employee_id}, location={self.location})"
    
    def __eq__(self, other):
        if not isinstance(other, MyEmployee_old):
            return NotImplemented
        return (self.name, self.employee_id, self.location) == (other.name, other.employee_id, other.location)


if __name__ == '__main__':

    employee1 = MyEmployee('John', 1, 'London')
    employee2 = MyEmployee('Joe', 2, 'New York')
    employee3 = MyEmployee('John', 1, 'London')
    print(employee1)
    print(employee1 == employee2)
    print(employee1 == employee3)
    employee11 = MyEmployee_old('John', 11, 'London')
    employee21 = MyEmployee_old('Joe', 21, 'New York')
    employee31 = MyEmployee_old('John', 11, 'London')
    print(employee11)
    print(employee11 == employee21)
    print(employee11 == employee31)
