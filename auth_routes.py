from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.get('/')
async def test():
    return {"message":"Hello World"}