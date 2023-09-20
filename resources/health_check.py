from fastapi import APIRouter

router = APIRouter(
    prefix="/common",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

@router.get("/health_check")
def health_check():
    return{
        "status":"ok"
    }