from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, db

app = FastAPI()

models.Base.metadata.create_all(bind=db.engine)

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(db.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/magazines/", response_model=list[schemas.Magazine])
def read_magazines(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    magazines = crud.get_magazines(db, skip=skip, limit=limit)
    return magazines

@app.post("/magazines/", response_model=schemas.Magazine)
def create_magazine(magazine: schemas.MagazineCreate, db: Session = Depends(db.get_db)):
    return crud.create_magazine(db=db, magazine=magazine)

@app.get("/plans/", response_model=list[schemas.Plan])
def read_plans(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    plans = crud.get_plans(db, skip=skip, limit=limit)
    return plans

@app.post("/plans/", response_model=schemas.Plan)
def create_plan(plan: schemas.PlanCreate, db: Session = Depends(db.get_db)):
    return crud.create_plan(db=db, plan=plan)

@app.get("/subscriptions/", response_model=list[schemas.Subscription])
def read_subscriptions(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    subscriptions = crud.get_subscriptions(db, user_id=user_id, skip=skip, limit=limit)
    return subscriptions

@app.post("/subscriptions/", response_model=schemas.Subscription)
def create_subscription(subscription: schemas.SubscriptionCreate, db: Session = Depends(db.get_db)):
    return crud.create_subscription(db=db, subscription=subscription)

@app.put("/subscriptions/{subscription_id}", response_model=schemas.Subscription)
def deactivate_subscription(subscription_id: int, db: Session = Depends(db.get_db)):
    return crud.deactivate_subscription(db=db, subscription_id=subscription_id)