from fastapi import APIRouter, HTTPException

from chanceapi.models.responses import ChanceSet

router = APIRouter(prefix="/generate", tags=["generator"])

@router.get("/", response_model=ChanceSet)
def generate_numbers():
    return ChanceSet()