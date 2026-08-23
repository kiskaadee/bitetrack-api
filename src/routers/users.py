import uuid
from datetime import UTC, date, datetime

from fastapi import APIRouter

from src.schemas.users import UserResponse, UserUpdate

router = APIRouter()

# Mocks
def get_user(user_id: uuid.UUID) -> UserResponse:
    """This is a mock of the actual controller yet to be implemented"""
    dummy_user = {
        "firstname": "Mellon",
        "lastname": "Collie",
        "nickname": "",
        "email": "melcol@smpumpk.ink",
        "dob": date(1995, 10, 23),
        "role": "staff",
        "modified_at": datetime(2026, 2, 18, tzinfo=UTC),
    }
    return UserResponse(id=user_id, **dummy_user)


def update_user(user_id: uuid.UUID, patch: UserUpdate, session="session") -> UserResponse:
    """This is a mock of the actual controller yet to be implemented"""
    print(f"Used {session}")
    user = get_user(user_id)
    patch_dict = patch.model_dump(exclude_unset=True)
    for field, value in patch_dict.items():
        setattr(user, field, value)
    user.modified_at = datetime.now(tz=UTC)
    return user


# Endpoints

@router.get("", response_model=list[UserResponse], status_code=200)
@router.get("/", response_model=list[UserResponse], status_code=200)
async def get_all_users() -> list[UserResponse]:
    """Placeholder endpoint"""
    return [get_user(uuid.uuid4())]


@router.get("/me", response_model=UserResponse, status_code=200)
async def get_my_profile() -> UserResponse:
    dummy_id = uuid.UUID("12345678-1234-5678-1234-567812345678")
    return get_user(dummy_id)


@router.patch("/me", response_model=UserResponse, status_code=200)
async def patch_my_profile(patch_data: UserUpdate) -> UserResponse:
    dummy_id = uuid.UUID("12345678-1234-5678-1234-567812345678")
    return update_user(dummy_id, patch_data)


@router.get("/{user_id}", response_model=UserResponse, status_code=200)
async def get_user_by_id(user_id: uuid.UUID) -> UserResponse:
    return get_user(user_id)

