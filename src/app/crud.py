from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        username=user.username, email=user.email, hashed_password=fake_hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_magazines(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Magazine).offset(skip).limit(limit).all()


def create_magazine(db: Session, magazine: schemas.MagazineCreate):
    db_magazine = models.Magazine(**magazine.dict())
    db.add(db_magazine)
    db.commit()
    db.refresh(db_magazine)
    return db_magazine


def get_plans(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Plan).offset(skip).limit(limit).all()


def create_plan(db: Session, plan: schemas.PlanCreate):
    db_plan = models.Plan(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan


def get_subscriptions(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return (
        db.query(models.Subscription)
        .filter(
            models.Subscription.user_id == user_id,
            models.Subscription.is_active == True,
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_subscription(db: Session, subscription: schemas.SubscriptionCreate):
    db_subscription = models.Subscription(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription


def deactivate_subscription(db: Session, subscription_id: int):
    db_subscription = (
        db.query(models.Subscription)
        .filter(models.Subscription.id == subscription_id)
        .first()
    )
    if db_subscription:
        db_subscription.is_active = False
        db.commit()
        db.refresh(db_subscription)
    return db_subscription
