from fastapi import APIRouter
from app.services.expert_service import get_experts_by_field

router = APIRouter()

@router.get("/")
async def get_experts(field: str | None = None):
    """
    Get a list of experts, optionally filtered by field.
    """
    return get_experts_by_field(field)
