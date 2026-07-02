from fastapi import FastAPI, Depends, HTTPException
from app.schemas import Create_note, note_response, UpdateNote, CreateUser, UserResponse, LoginRequest
from app.db import get_async_session, create_db_and_tables
from app.models import Note, User
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select
from app.security import hash_password, verify_password

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
@app.post("/note", response_model=note_response, status_code=201)
async def Create_note(
        note: Create_note,
        session: AsyncSession = Depends(get_async_session),
):
    new_note= Note(
        heading= note.heading,
        title=note.title,
        content= note.content,
        priority= note.priority,
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

@app.delete("/notes/{note_id}")
async def delete_note(
        note_id: str, session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(
        select(Note).where(Note.id == note_id)
    )
    note = result.scalar_one_or_none()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    await session.delete(note)
    await session.commit()
    return {
        "message": "Note deleted successfully"
    }
@app.put("/notes/{note_id}", response_model=note_response, status_code=200)
async def update_note(
        note_id: str,
        updated_note: UpdateNote,
        session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(
        select(Note).where(Note.id == note_id)
    )
    note = result.scalar_one_or_none()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    note.heading = updated_note.heading
    note.title = updated_note.title
    note.content = updated_note.content
    note.priority = updated_note.priority
    note.tags = updated_note.tags

    await session.commit()
    await session.refresh(note)
    return note

@app.post("/Register", response_model= UserResponse)

async def CreateUser(
        user: CreateUser,
        session: AsyncSession = Depends(get_async_session),
):
    new_user = User(
        email_id= user.EmailId,
        user_name= user.UserName,
        password_hash= hash_password(user.Password),

    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

@app.post("/login")
async def login(
        user: LoginRequest,
        session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(
        select(User).where((User.email_id == user.identifier) |
                            (User.user_name == user.identifier)
                           ))
    db_user = result.scalar_one_or_none()
    if user is None or not verify_password(user.password, db_user.password_hash ):
        raise HTTPException(status_code=404, detail="Username or password is invalid ")





