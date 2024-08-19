from pydantic import BaseModel, Field, field_validator
from datetime import datetime
import json

class Address(BaseModel):
    street: str
    city: str
    state: str
    postcode: str

class Employee(BaseModel):

    name: str
    id: int
    location: str
    address: Address
    email: str
    manages: list[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)


    @field_validator('name')
    def name_must_be_capitalised(v: str):
        if not v.istitle():
            raise ValueError("Name must be capitalised")
        return v

if __name__ == '__main__':
    # if we use 'john' as name: 
    # pydantic_core._pydantic_core.ValidationError: 3 validation errors for Employee
    # name
    # Value error, Name must be capitalised [type=value_error, input_value='john', input_type=str]
    # For further information visit https://errors.pydantic.dev/2.8/v/value_error
    employee_1 = Employee(
        name='John',
        id='1',
        location='London',
        address={
            'street': '123 High St',
            'city': 'London',
            'state': 'London',
            'postcode': 'SW1 1R1',
        },
        email = 'john.developer@test.com'
    )
    print(employee_1)
    # name='John' id=1 location='London' address=Address(street='123 High St', city='London', state='London', postcode='SW1 1R1') email='john.developer@test.com' manages=[] created_at=datetime.datetime(2024, 8, 18, 11, 59, 47, 14133)
    json_schema = Employee.model_json_schema()
    print(json.dumps(json_schema, indent=2))