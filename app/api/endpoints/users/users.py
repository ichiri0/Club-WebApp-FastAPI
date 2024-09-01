"""
User Endpoints Module
"""


from api import deps
from models import User, UserSchema, UserCreateSchema

from fastapi import APIRouter, HTTPException, Depends
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.transactions import in_transaction
from typing import List, Optional


router = APIRouter()


@router.get('/users' , response_model=Optional[List[UserSchema]])
async def get_users():
    return await UserSchema.from_queryset(User.all())


@router.post("/", response_model=UserSchema)
async def create_user(user: UserCreateSchema): # type: ignore
    print(user)
    user_obj = await User.create(**user.dict(exclude_unset=True))
    await user_obj.save()
    return await UserSchema.from_tortoise_orm(user_obj)


@router.get("/{user_id}", response_model=UserSchema, responses={404: {"model": HTTPNotFoundError}})
async def get_user(user_id: int):
    user_obj = await User.get(id=user_id)
    print(user_obj)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    return await UserSchema.from_tortoise_orm(user_obj)


@router.get("/tg/{user_id}", response_model=UserSchema, responses={404: {"model": HTTPNotFoundError}})
async def get_user_by_tg_id(user_id: int):
    user_obj = await User.get(tg_user_id=user_id)
    print(user_obj)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    return await UserSchema.from_tortoise_orm(user_obj)


@router.put("/tg/{user_id}", response_model=UserSchema, responses={404: {"model": HTTPNotFoundError}})
async def update_user_by_tg_id(user_id: int, user: UserCreateSchema): # type: ignore
    print(user)
    user_obj = await User.get(tg_user_id=user_id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    user_obj.update_from_dict(user.dict())
    await user_obj.save()
    return await UserSchema.from_tortoise_orm(user_obj)


@router.delete("/tg/{user_id}", responses={404: {"model": HTTPNotFoundError}})
async def delete_user_by_tg_id(user_id: int):
    user_obj = await User.get(tg_user_id=user_id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    await user_obj.delete()
    return {"message": "User deleted successfully"}


