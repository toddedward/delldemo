from typing import List, Union

from pydantic import BaseModel


class ColorBase(BaseModel):
    name: str
    price: int

class ColorCreate(ColorBase):
    pass

class Color(ColorBase):
    id: int

    class Config:
        orm_mode = True


class MemoryBase(BaseModel):
    name: str
    price: int

class MemoryCreate(MemoryBase):
    pass

class Memory(MemoryBase):
    id: int

    class Config:
        orm_mode = True


class LaptopBase(BaseModel):
    color: str
    memory: str

class LaptopCreate(LaptopBase):
    pass

class Laptop(LaptopBase):
    # id: int
    price: int

    class Config:
        orm_mode = True

