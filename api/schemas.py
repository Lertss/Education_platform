import re
import uuid

from fastapi import HTTPException
from pydantic import BaseModel, ConfigDict, EmailStr, field_validator


LETTER_MATCH_PATTERN = re.compile(r"^[a-zA-Z\-]+$")


class ShowUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr

    @field_validator("name")
    @classmethod
    def name_must_contain_space(cls, value: str) -> str:
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422,
                detail="Name should contains only letters",
            )
        return value.title()

    @field_validator("surname")
    @classmethod
    def surname_must_contain_space(cls, value: str) -> str:
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422,
                detail="Name should contains only letters",
            )
        return value.title()
