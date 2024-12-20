from pydantic import BaseModel
from typing import Optional
from datetime import date


class SupplierBase(BaseModel):
    name: str
    contact: Optional[str] = None
    address: Optional[str] = None


class SupplierCreate(SupplierBase):
    pass


class Supplier(SupplierBase):
    id: int

    class Config:
        from_attributes = True


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Optional[float] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


class UnitBase(BaseModel):
    name: str
    description: Optional[str] = None


class UnitCreate(UnitBase):
    pass


class Unit(UnitBase):
    id: int

    class Config:
        from_attributes = True


class OrderBase(BaseModel):
    supplier_id: int
    item_id: int
    unit_id: int
    quantity: float
    price: float
    total: float
    payment_cycle: str
    payment_method: str = "계좌이체"
    client: str
    notes: Optional[str] = None
    date: Optional[date] = None


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: int
    date: Optional[str]
    quantity: float
    supplier_id: int
    item_id: int
    unit_id: int
    supplier: Supplier
    item: Item
    unit: Unit
    price: float
    total: float
    payment_cycle: str
    payment_method: str
    client: str
    notes: Optional[str] = None

    class Config:
        from_attributes = True
