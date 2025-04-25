from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str = 'Himalay'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float = Field(gt=0,lt=10,default=6)

new_student={'age':'32','email':'abc@gmail.com','cgpa':8}
student = Student(**new_student)
dict_student=dict(student)
student_json = student.model_dump_json()

print(dict_student)
print(student_json)

