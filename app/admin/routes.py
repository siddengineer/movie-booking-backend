# # app/admin/routes.py
# from fastapi import APIRouter

# router = APIRouter(prefix="/admin", tags=["Admin"])

# @router.get("/ping")
# def ping():
#     return {"message": "Admin route works!"}
from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/movies")
def create_movie():
    return {"msg": "Movie created"}
