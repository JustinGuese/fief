from typing import Any, Dict
from fastapi_users import schemas
from pydantic import UUID4, root_validator, Field

from fief.models import User
from fief.schemas.tenant import TenantEmbedded


class UserRead(schemas.BaseUser):
    tenant_id: UUID4
    tenant: TenantEmbedded
    fields: Dict[str, Any]

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    pass


class UserCreateInternal(UserCreate):
    """
    Utility model so that we can hook into the logic of UserManager.create
    and add some attributes before persisting into database.
    """

    tenant_id: UUID4


class UserUpdate(schemas.BaseUserUpdate):
    pass
