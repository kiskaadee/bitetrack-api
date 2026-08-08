from fastapi import APIRouter

router = APIRouter()


@router.get("")
@router.get("/")
async def fetch_all_customers():
    # To-do
    return {"status": "Coming soon."}
