from fastapi import FastAPI
from product_routes import router 
from database import create_db_and_tables

app = FastAPI()

create_db_and_tables()

app.include_router(router, prefix="/api", tags=["Produtos"])

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Gerenciamento de Produtos"}
