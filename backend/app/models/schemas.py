from typing import List, Optional, Any
from pydantic import BaseModel

class UserPreferences(BaseModel):
    field: str
    noveltyLevel: int
    goal: str

class IdeaRequest(BaseModel):
    field: str
    noveltyLevel: int

class Idea(BaseModel):
    id: str
    title: str
    description: str
    marketPotential: str
    feasibility: str
    noveltyScore: int
    field: str
    researchCitations: List[str]

class Expert(BaseModel):
    id: str
    name: str
    role: str
    field: str
    avatar: str
    domainAuthority: int
    publications: int
    bio: str
