import uuid
from datetime import UTC, datetime

from fastapi import APIRouter

from src.schemas.users import UserRegister, UserResponse

router = APIRouter()

# TODO: Implement POST /register
# 1. Accept UserRegister schema
# 2. Return UserResponse schema
# 3. Use dummy/fake data for now

def new_user(user_data: UserRegister, session="session"):
    print(f"Used {session}")
    # process password, insert to database
    return UserResponse(id=uuid.uuid4(), modified_at=datetime.now(tz=UTC), **user_data.model_dump())


@router.post("/register", response_model=UserResponse, status_code=201)
async def register_user(user_data: UserRegister) -> UserResponse:
    """
    Dummy endpoint for user registration.
    Performs auto-validation of incoming payloads and returns mock database fields.
    """
    return new_user(user_data)
