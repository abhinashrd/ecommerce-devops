from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    order_id: int
    item_name: str
    quantity: int

@app.get("/")
def root():
    return {"message": "Order Service is running"}

@app.post("/place-order")
def place_order(order: Order):
    return {
        "status": "Order placed",
        "order_details": order
    }
