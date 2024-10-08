"""
App Endpoints Module
"""

from fastapi import APIRouter

from . import users

router = APIRouter()

router.include_router(users.router)

