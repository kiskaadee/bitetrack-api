from fastapi import APIRouter

router = APIRouter()


# health check
@router.get("/")
async def health():
    return {"message": "Server is healthy!"}
