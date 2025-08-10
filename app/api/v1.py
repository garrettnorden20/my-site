from __future__ import annotations

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import get_session
from .. import models

router = APIRouter()


@router.get("/sample")
async def sample() -> dict[str, str]:
    return {"message": "ok"}


@router.get("/notes", response_model=List[dict[str, str]])
async def get_notes(db: Session = Depends(get_session)):
    notes = db.query(models.Note).all()
    return [{"id": n.id, "content": n.content} for n in notes]


@router.post("/notes", response_model=dict)
async def create_note(data: dict, db: Session = Depends(get_session)):
    content = data.get("content")
    if not content:
        raise HTTPException(status_code=400, detail="content required")
    note = models.Note(content=content)
    db.add(note)
    db.commit()
    db.refresh(note)
    return {"id": note.id, "content": note.content}
