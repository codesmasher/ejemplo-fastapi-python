from fastapi import APIRouter, HTTPException

from models.user_model import UserModel

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/name/{username}")
async def sheach_user_by_login(username: str):
    """
    Obtener dados del usuario con su email/username
    """
    user = await UserModel.search_for_username(username)

    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"Username {username} no existe."
        )
    return user
