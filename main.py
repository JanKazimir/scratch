from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class DoubleInput(BaseModel):
    number: int

@app.post("/double/")
def ask_for_double(num: DoubleInput):
    return {"Your number doubled" : num.number *2}
    

class Salary(BaseModel):
    salary: int
    bonus : int
    taxes: int


@app.post("/salary/")
def final_salary_calculation(sal: Salary):
    final_pay = sal.salary + sal.bonus - sal.taxes
    return {"final pay:": final_pay}

        
        


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/double/{number}")
def double(number :int):
    return {"Your number doubled" : {number*2}}


