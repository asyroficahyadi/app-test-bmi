from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root(height: float = Query (..., gt=0), weight: float = (Query (..., gt=0))):
    height /= 100
    bmi = round(weight / (height * height), 2)
    if bmi < 18.5:
        return JSONResponse(
            content={
                "bmi": bmi,
                "label": "Underweight"},
            status_code=200)
    elif bmi >= 18.5 and bmi <= 24.9:
        return JSONResponse(
            content={
                "bmi": bmi,
                "label": "Normal weight"},
            status_code=200)
    elif bmi >= 25.0:
        return JSONResponse(
            content={
                "bmi": bmi,
                "label": "Overweight"},
            status_code=200)