from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/generate", tags=["generator"])

@router.get("/", response_model=ChanceSet)
def generate_numbers():
    pass