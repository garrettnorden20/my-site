from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import text  # <-- add
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from .settings import settings
from .db import get_session, engine, Base
from .api import api_router
from . import models
from .tasks.sitemap import rebuild_sitemap

app = FastAPI(title=settings.app_name)
app.include_router(api_router, prefix="/api")
templates = Jinja2Templates(directory="app/views")

@app.on_event("startup")
async def startup() -> None:
    Base.metadata.create_all(bind=engine)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(rebuild_sitemap, "cron", hour=0)
    scheduler.start()
    app.state.scheduler = scheduler

@app.on_event("shutdown")
async def shutdown() -> None:
    scheduler: AsyncIOScheduler = app.state.scheduler
    await asyncio.get_event_loop().run_in_executor(None, scheduler.shutdown, False)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/notes", response_class=HTMLResponse)
async def notes_list(request: Request, db: Session = Depends(get_session)):
    notes = db.query(models.Note).order_by(models.Note.id.desc()).all()
    return templates.TemplateResponse("partials/notes_items.html", {"request": request, "notes": notes})

@app.post("/notes", response_class=HTMLResponse)
async def notes_create(request: Request, content: str = Form(...), db: Session = Depends(get_session)):
    note = models.Note(content=content)
    db.add(note)
    db.commit()
    db.refresh(note)
    notes = db.query(models.Note).order_by(models.Note.id.desc()).all()
    return templates.TemplateResponse("partials/notes_items.html", {"request": request, "notes": notes})

@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/readyz")
async def readyz(db: Session = Depends(get_session)) -> dict[str, str]:
    db.execute(text("SELECT 1"))
    return {"status": "ready"}
