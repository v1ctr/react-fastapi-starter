from datetime import datetime
from fastapi import APIRouter, Body, Depends  
from starlette.status import HTTP_201_CREATED

from app.models.user import UserCreate, UserPublic  
from app.db.repositories.users import UsersRepository  
from app.api.dependencies.database import get_repository  

router = APIRouter()

@router.get("/me")
async def user_me() -> dict:
    user = {
        'id': 1,
        'email': 'john.doe@dummy.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'created_at': datetime.utcnow()
    }

    return user


@router.post("/", response_model=UserPublic, name="users:create-user", status_code=HTTP_201_CREATED)
async def create_new_user(
    new_user: UserCreate = Body(..., embed=True),
    users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
) -> UserPublic:
    created_user = await users_repo.create_user(new_user=new_user)
    return created_user

