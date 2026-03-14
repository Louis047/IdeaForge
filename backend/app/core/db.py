from supabase import create_client, Client
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

def get_supabase_client() -> Client | None:
    if not settings.NEXT_PUBLIC_SUPABASE_URL or not settings.SUPABASE_SERVICE_ROLE_KEY:
        logger.warning("Supabase credentials not found. DB operations will fail.")
        return None
    
    return create_client(
        settings.NEXT_PUBLIC_SUPABASE_URL,
        settings.SUPABASE_SERVICE_ROLE_KEY
    )

