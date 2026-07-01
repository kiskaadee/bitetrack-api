from fastapi import APIRouter

## Later:
# from .users import router as users
# from .orders import router as orders
# from .products import router as products
from .info import router as system_info

# Aggregate all application routers
router = APIRouter()

router.include_router(system_info, tags=["System Info"])  ## root level; no prefix
## Later:
# routers.include_router(users, prefix="/users", tags="Users")
# routers.include_router(categories, prefix="/categories", tags="Categories")
# routers.include_router(products, prefix="/producs", tags="Products")
# routers.include_router(orders, prefix="/orders", tags="Orders")


__all__ = ["router"]
