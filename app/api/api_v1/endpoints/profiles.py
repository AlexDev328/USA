from typing import Any
from fastapi import APIRouter, Depends

from app import models, schemas
from app.api import deps
from app.models import User
from app.models.profile import Profile

router = APIRouter()


@router.get("/me", response_model=schemas.ProfileBase)
async def read_user_me(
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user

