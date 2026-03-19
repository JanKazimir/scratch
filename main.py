from fastapi import FastAPI, Request
from pydantic import BaseModel, StrictInt
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError



app = FastAPI()

class DoubleInput(BaseModel):
    number: int

@app.post("/double/")
def ask_for_double(num: DoubleInput):
    return {"Your number doubled" : num.number *2}
    

class Salary(BaseModel):
    salary: StrictInt
    bonus: StrictInt
    taxes: StrictInt


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    missing_fields = []

    for error in errors:
        field_name = error["loc"][-1]

        if error["type"] == "missing":
            missing_fields.append(field_name)
        elif error["type"] in {"int_type", "int_parsing"}:
            return JSONResponse(
                status_code=422,
                content={"error": "expected numbers, got strings."},
            )

    if missing_fields:
        forgot = ", ".join(missing_fields)
        return JSONResponse(
            status_code=422,
            content={
                "error": (
                    "3 fields expected (salary, bonus, taxes). "
                    f"You forgot: {forgot}."
                )
            },
        )

    return JSONResponse(
        status_code=422,
        content={"error": "Invalid request body."},
    )


@app.post("/salary/")
def final_salary_calculation(sal: Salary):
    final_pay = sal.salary + sal.bonus - sal.taxes
    return {"result": final_pay}

        
        


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/double/{number}")
def double(number :int):
    return {"Your number doubled" : {number*2}}

