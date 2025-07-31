from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Payment(BaseModel):
    payment_id: int
    order_id: int
    amount: float

@app.get("/")
def root():
    return {"message": "Payment Service is running"}

@app.post("/pay")
def make_payment(payment: Payment):
    return {
        "status": "Payment successful",
        "payment_details": payment
    }
