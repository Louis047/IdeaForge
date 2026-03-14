from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import UserPreferences
from app.core.db import get_supabase_client
from supabase import Client

router = APIRouter()

@router.post("/preferences")
async def save_preferences(prefs: UserPreferences, db: Client = Depends(get_supabase_client)):
    """
    Save user onboarding preferences.
    """
    if not db:
        return {"status": "success", "preferences": prefs}
        
    try:
        # Assuming there is a user_preferences table
        data = prefs.model_dump()
        response = db.table("user_preferences").upsert(data).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
