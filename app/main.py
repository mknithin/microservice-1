from fastapi import FastAPI

app = FastAPI()


@app.get("/public")
async def get_public():
    return {"message": "Do you like public speaking?"}

@app.get("/private")
async def get_luck():
    return {"message": "Do you like private speaking?"}

@app.get("/luck")
async def get_luck():
    return {"message": "Do you feel lucky, punk?"}

@app.get("/say")
async def get_say():
    return {"message": "I am saying something"}

@app.get("/wish")
async def get_wish():
    return {"message": "Hello there good night!"}


@app.get("/")
async def root():
    return {"message": "Hello World"}



