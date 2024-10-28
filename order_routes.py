from fastapi import APIRouter

order_router = APIRouter()

@order_router.get('/')
async def test():
    return {"message":"Hello World"}