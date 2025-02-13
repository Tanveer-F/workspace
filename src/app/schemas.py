from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class MagazineBase(BaseModel):
    name: str
    description: Optional[str] = None
    base_price: float


class MagazineCreate(MagazineBase):
    pass


class Magazine(MagazineBase):
    id: int

    class Config:
        orm_mode = True


class PlanBase(BaseModel):
    title: str
    description: Optional[str] = None
    renewal_period: int
    discount: float
    tier: int


class PlanCreate(PlanBase):
    pass


class Plan(PlanBase):
    id: int

    class Config:
        orm_mode = True


class SubscriptionBase(BaseModel):
    user_id: int
    magazine_id: int
    plan_id: int
    price: float
    renewal_date: datetime
    is_active: bool


class SubscriptionCreate(SubscriptionBase):
    pass


class Subscription(SubscriptionBase):
    id: int

    class Config:
        orm_mode = True
