from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Registration(BaseModel):
  name: str
  email: str
  age: int
  password: str
  student: bool = True
  Working: Optional[str] = None
  

List = [{"name": "Anthony", "email":"tony@gmail.com", "age": 26, "password": "password", "student": "False", "id": 1}]
value = 2


@app.get("/")
def home():
  return{"msg": "Ant-Index welcome to the world of backends"}


@app.post("/SignUp", status_code= status.HTTP_201_CREATED)
def SignUp(register: Registration):
  global value
  students_info = register.dict()
  students_info['id'] = value
  List.append(students_info)
  value+=1
  return({"data": List})


@app.get("/view_info")
def view():
  return({"data": List})

