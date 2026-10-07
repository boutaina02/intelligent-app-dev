from fastapi import FastAPI

app = FastAPI(title="Student Management API")

@app.get("/")
def home():
    return {"message": "Student Management API is running"}

@app.get("/students")
def get_students():
    return [
        {"id": 1, "name": "Alice", "age": 21},
        {"id": 2, "name": "Bob", "age": 22}
    ]