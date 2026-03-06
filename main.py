from fastapi import FastAPI
app = FastAPI(title="API Захаровой Надежды", version="1.0.3")

@app.get("/")
def home():
    return {"message": "Привет, мир!", "author": "Захарова"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/about")
def about():
    return {"name": "Захарова", "project": "Учебный проект FastAPI"}