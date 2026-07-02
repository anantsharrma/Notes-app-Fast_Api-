from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field

class Create_note(BaseModel):
    heading: str
    title: str
    tags: list[str] = Field(default_factory=list)
    content: str
    priority: Literal["high", "low", "medium"] = "low"

class note_response(BaseModel):
    heading: str
    id: str
    title: str
    tags: list[str] = Field(default_factory=list)
    content: str
    priority: Literal["high", "low", "medium"] = "low"
    date: datetime
    model_config = { "from_attributes": True}

class UpdateNote(BaseModel):
    heading: str | None = None
    title: str | None = None
    content: str | None = None
    priority: str | None = None
    tags: list[str] | None = None

class CreateUser(BaseModel):
    UserName: str
    EmailId: str
    Password: str

class UserResponse(BaseModel):
    user_name: str
    email_id: str
    user_id: str
    model_config = { "from_attributes": True}

class LoginRequest(BaseModel):
    identifier: str
    password: str

