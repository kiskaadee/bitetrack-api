from fastapi import APIRouter

router = APIRouter()


# health check
@router.get("/health")
@router.get("/healthz")
async def health():
    return {"message": "Server is healthy!"}
