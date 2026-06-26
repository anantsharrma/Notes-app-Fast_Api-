from fastapi import FastAPI, Depends
from app.schemas import Create_note, note_response
from app.db import get_async_session, create_db_and_tables
from app.models import Note
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from contextlib import asynccontextmanager
from sqlalchemy import select
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
@app.post("/create_note")
async def Create_note(
        note: Create_note,
        session: AsyncSession = Depends(get_async_session),
):
    new_note= Note(
        heading= note.heading,
        content= note.content,
        priority= note.priority,
        title= note.title,
        tags= note.tags
    )
    session.add(new_note)
    await session.commit()
    await session.refresh(new_note)
    return new_note

@app.get("/notes",
         response_model= list[note_response])
async def get_notes(
        session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(
        select(Note)
    )
    notes = result.scalars().all()
    return notes
