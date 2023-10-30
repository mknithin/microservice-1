from fastapi import FastAPI

app = FastAPI()

@app.get("/wish")
async def get_wish():
    return {"message": "Hello there good morning!"}


@app.get("/")
async def root():
    return {"message": "Hello World"}



