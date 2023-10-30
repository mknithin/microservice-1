from fastapi import FastAPI

app = FastAPI()

@app.get("/say")
async def get_say():
    return {"message": "I am saying something"}

@app.get("/wish")
async def get_wish():
    return {"message": "Hello there good night!"}


@app.get("/")
async def root():
    return {"message": "Hello World"}



