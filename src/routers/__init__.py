from fastapi import APIRouter

from .auth import router as auth
from .info import router as system_info
from .users import router as users

# Aggregate all application routers
router = APIRouter()
system_router = APIRouter()

system_router.include_router(system_info, tags=[""])
router.include_router(auth, prefix="/auth", tags=["Auth"])
router.include_router(users, prefix="/users", tags=["Users"])

__all__ = ["router"]
