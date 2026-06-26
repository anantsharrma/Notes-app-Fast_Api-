from sqlalchemy import Column, String, DateTime, JSON
from app.db import Base
from datetime import datetime
import uuid
from sqlalchemy.orm import mapped_column, Mapped

class Note(Base):
    __tablename__ = "notes"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )
    heading:Mapped[str] = mapped_column(String)
    title:Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)
    date: Mapped[str] = mapped_column(DateTime, default=datetime.now)
    priority: Mapped[str] = mapped_column(String)
    tags: Mapped[list] = mapped_column(JSON)
    





