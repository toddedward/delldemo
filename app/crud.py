from sqlalchemy.orm import Session

from . import models, schemas


def get_color_by_name(db: Session, name: str):
    return db.query(models.Color).filter(models.Color.name == name).first()

def get_colors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Color).offset(skip).limit(limit).all()

def create_color(db: Session, color: schemas.ColorCreate):
    db_color = models.Color(name=color.name, price=color.price)
    db.add(db_color)
    db.commit()
    db.refresh(db_color)
    return db_color

def delete_color(db: Session, color: schemas.Color):
    db_color = db.query(models.Color).filter(models.Color.name == color.name).first()
    # db_color = models.Color(name=color.name, price=color.price)
    db.delete(db_color)
    db.commit()


def get_memory_by_name(db: Session, name: str):
    return db.query(models.Memory).filter(models.Memory.name == name).first()

def get_memory(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Memory).offset(skip).limit(limit).all()

def create_memory(db: Session, memory: schemas.MemoryCreate):
    db_memory = models.Memory(name=memory.name, price=memory.price)
    db.add(db_memory)
    db.commit()
    db.refresh(db_memory)
    return db_memory

def delete_memory(db: Session, memory: schemas.Memory):
    db_memory = db.query(models.Memory).filter(models.Memory.name == memory.name).first()
    db.delete(db_memory)
    db.commit()

def create_laptop(db: Session, color: schemas.ColorCreate, memory: schemas.MemoryCreate):
    db_laptop = models.Laptop(color=color.name, memory=memory.name, price=memory.price + 1000)
    return db_laptop

