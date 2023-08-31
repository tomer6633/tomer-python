from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return "he"

@app.get("/posts")
def get_post():
    return{"date: this is ur posts"}


@app.post("/create-post")
def createPost(payLoad: dict = Body(...)):
    print(payLoad)
    return