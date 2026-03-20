from fasttest import FastAPI
from pydantic import BaseModel


app = FastAPI()

class DoubleInput(BaseModel):
    number: int


@app.post("/double/")
def ask_for_double(num: DoubleInput):
    return {"Your number doubled" : {num.number *2}}
    

@app.get("/")
async def root():
    return {"message": "testing World"}

@app.get("/double/{number}")
def double(number :int):
    return {"Your number doubled" : {number*2}}



