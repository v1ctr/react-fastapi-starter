from uuid import UUID
from typing import Union
from pydantic import BaseModel


class CoreModel(BaseModel):
    """
    Any common logic to be shared by all models goes here.
    """
    pass


class IDModelMixin(BaseModel):
    id: Union[str, UUID]

    class Config:
        orm_mode = True