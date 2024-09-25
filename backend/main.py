from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Hello" : "World!"}

@app.get("/profile/{username}")
def profile(username: str) -> Union[dict, str]:
    return {"username": username}

@app.get("/login")
def login(username: str, password: str) -> Union[dict, str]:
    if username and password:
        return profile(username)