from fastapi import APIRouter, HTTPException, Depends
from app.models.schemas import Idea
from app.core.db import get_supabase_client
from supabase import Client
from typing import List

router = APIRouter()

@router.get("/ideas", response_model=List[Idea])
async def get_saved_ideas(db: Client = Depends(get_supabase_client)):
    """
    Get all saved ideas for the current user.
    """
    if not db:
        # Mock response if DB not configured
        return []
    
    try:
        # Assuming RLS handles user scoping, or we'd extract user_id from token
        response = db.table("saved_ideas").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ideas", response_model=Idea)
async def save_idea(idea: Idea, db: Client = Depends(get_supabase_client)):
    """
    Save an idea to the user's dashboard.
    """
    if not db:
        return idea

    try:
        data = idea.model_dump()
        response = db.table("saved_ideas").insert(data).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/ideas/{id}")
async def delete_idea(id: str, db: Client = Depends(get_supabase_client)):
    """
    Delete a saved idea.
    """
    if not db:
        return {"status": "success", "id": id}
        
    try:
        db.table("saved_ideas").delete().eq("id", id).execute()
        return {"status": "success", "id": id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
