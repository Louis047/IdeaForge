from fastapi import APIRouter, HTTPException
from app.models.schemas import IdeaRequest, Idea
from app.services.idea_service import generate_ideas_with_agents
from typing import List

router = APIRouter()

@router.post("/generate", response_model=List[Idea])
async def generate_ideas(request: IdeaRequest):
    """
    Generate ideas based on user's field and novelty level.
    Uses CrewAI behind the scenes to research and synthesize.
    """
    try:
        ideas = await generate_ideas_with_agents(
            field=request.field,
            novelty_level=request.noveltyLevel
        )
        return ideas
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
