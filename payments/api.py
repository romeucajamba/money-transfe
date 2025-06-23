from ninja import Router

payments_router = Router()

@payments_router.post("/")
def transation(rquest):
    return {"message": "Payment transaction successful"}