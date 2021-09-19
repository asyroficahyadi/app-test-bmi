from fastapi import FastAPI

appbmi = FastAPI()

@appbmi.get("/")
async def root():
    return {
        "Main function"
    }