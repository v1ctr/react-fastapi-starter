from fastapi import APIRouter
from datetime import datetime

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

