import json

from controllers import user_controller

from fastapi import APIRouter, responses

router = APIRouter()


@router.get("/{id}")
async def get_user(
    id: str,
) -> responses.JSONResponse:
    try:
        user = user_controller.get_user(id)
        return responses.JSONResponse(user)
    except Exception as e:
        return responses.JSONResponse(status_code=500, content={"message": str(e)})


@router.post("/")
async def create_user(
    user: dict,
) -> responses.JSONResponse:
    try:
        user = await user_controller.create_user(user)
        return responses.JSONResponse(user, status_code=201)
    except Exception as e:
        return responses.JSONResponse(status_code=500, content={"message": str(e)})