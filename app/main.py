from fastapi import FastAPI

app = FastAPI()

@app.get("/say")
async def get_say():
    return {"message": "Say something!"}

@app.get("/wish")
async def get_wish():
    return {"message": "Hello there good morning!"}


@app.get("/")
async def root():
    return {"message": "Hello World"}



