from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/api")
def read_api():
    return {"message": "Hello from API!"}
