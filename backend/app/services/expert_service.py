from app.models.schemas import Expert

# Mock database of experts to serve as our base matching logic
MOCK_EXPERTS = [
    Expert(
        id="exp-1",
        name="Dr. Sarah Chen",
        role="AI Researcher",
        field="HealthTech",
        avatar="https://api.dicebear.com/7.x/avataaars/svg?seed=Sarah",
        domainAuthority=92,
        publications=45,
        bio="Specializes in medical imaging AI"
    ),
    Expert(
        id="exp-2",
        name="Prof. James Miller",
        role="FinTech Innovator",
        field="FinTech",
        avatar="https://api.dicebear.com/7.x/avataaars/svg?seed=James",
        domainAuthority=88,
        publications=12,
        bio="Former CTO of BlockPay"
    ),
    Expert(
        id="exp-3",
        name="Dr. Aisha Rahman",
        role="EdTech Specialist",
        field="EdTech",
        avatar="https://api.dicebear.com/7.x/avataaars/svg?seed=Aisha",
        domainAuthority=85,
        publications=23,
        bio="Focuses on adaptive learning systems"
    )
]

def get_experts_by_field(field: str | None = None) -> list[Expert]:
    """
    Retrieve experts filtered by field.
    """
    if field:
        # Simple exact match for now, could be expanded to semantic search
        return [e for e in MOCK_EXPERTS if e.field.lower() == field.lower()]
    return MOCK_EXPERTS
