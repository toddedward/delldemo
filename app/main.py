from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/colors", response_model=List[schemas.Color])
def read_colors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    colors = crud.get_colors(db, skip=skip, limit=limit)
    return colors


@app.post("/colors", response_model=schemas.Color)
def create_color(color_request: schemas.ColorCreate, db: Session = Depends(get_db)):
    db_color = crud.get_color_by_name(db, name=color_request.name)
    if db_color:
        raise HTTPException(status_code=400, detail="Color already exists")
    return crud.create_color(db=db, color=color_request)


@app.delete("/colors", response_model=schemas.Color)
def delete_color(color_request: schemas.ColorCreate, db: Session = Depends(get_db)):
    db_color = crud.get_color_by_name(db, name=color_request.name)
    if not db_color:
        raise HTTPException(status_code=400, detail="Color not found")
    return crud.delete_color(db=db, color=color_request)


@app.get("/memory", response_model=List[schemas.Memory])
def read_memory(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    memory = crud.get_memory(db, skip=skip, limit=limit)
    return memory


@app.post("/memory", response_model=schemas.Memory)
def create_memory(memory_request: schemas.MemoryCreate, db: Session = Depends(get_db)):
    db_memory = crud.get_memory_by_name(db, name=memory_request.name)
    if db_memory:
        raise HTTPException(status_code=400, detail="Memory already exists")
    return crud.create_memory(db=db, memory=memory_request)


@app.delete("/memory", response_model=schemas.Memory)
def delete_memory(memory_request: schemas.MemoryCreate, db: Session = Depends(get_db)):
    db_memory = crud.get_memory_by_name(db, name=memory_request.name)
    if not db_memory:
        raise HTTPException(status_code=400, detail="Memory not found")
    return crud.delete_memory(db=db, memory=memory_request)


@app.post("/laptop", response_model=schemas.Laptop)
def create_laptop(laptop_request: schemas.LaptopCreate, db: Session = Depends(get_db)):
    db_memory = crud.get_memory_by_name(db, name=laptop_request.memory)
    if not db_memory:
        raise HTTPException(status_code=400, detail="Memory not found")

    db_color = crud.get_color_by_name(db, name=laptop_request.color)
    if not db_color:
        raise HTTPException(status_code=400, detail="Color not found")

    return crud.create_laptop(db=db, color=db_color, memory=db_memory)
    #return JSONResponse(status_code=200, content={"message": f"{db_memory} {db_color}"})


