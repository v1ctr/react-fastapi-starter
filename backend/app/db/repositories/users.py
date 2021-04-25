from uuid import uuid4
from datetime import datetime
from app.db.tables.users import users_table
from app.db.repositories.base import BaseRepository
from app.models.user import UserCreate, UserUpdate, UserInDB


class UsersRepository(BaseRepository):
    """"
    All database actions associated with the User resource
    """

    async def create_user(self, *, new_user: UserCreate) -> UserInDB:
        query_values = new_user.dict()
        query_values["id"]=uuid4()
        query_values["created_at"]=datetime.utcnow()
        query_values["hashed_password"]=query_values["password"]
        del query_values["password"]
        query = users_table.insert().values(**query_values)
        id = await self.db.execute(query)
        return UserInDB(**query_values)

