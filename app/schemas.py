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
    title: str
    tags: list[str] = Field(default_factory=list)
    content: str
    priority: Literal["high", "low", "medium"] = "low"
    date: datetime
    model_config = { "from_attributes": True}

