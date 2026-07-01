from fastapi import APIRouter

# from .orders import router as orders
# from .products import router as products
from .info import router as system_info

## Later:
from .users import router as users

# Aggregate all application routers
router = APIRouter()
system_router = APIRouter()

system_router.include_router(system_info, tags=[""])
router.include_router(users, prefix="/users", tags=["Users"])
## Later:
# routers.include_router(categories, prefix="/categories", tags="Categories")
# routers.include_router(products, prefix="/producs", tags="Products")
# routers.include_router(orders, prefix="/orders", tags="Orders")


__all__ = ["router"]
