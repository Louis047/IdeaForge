# IdeaForge Backend README

## Getting Started

1. Set up your environment variables:
`cp .env.example .env`

2. Fill in the `.env` file with:
   - Supabase URL & Service Role Key
   - Hugging Face Token (if `LLM_PROVIDER=huggingface`)
   
3. Install dependencies:
`pip install -r requirements.txt`

4. Run the development server:
`uvicorn app.main:app --reload`

5. Visit the Swagger UI for testing:
`http://127.0.0.1:8000/docs`

## Technical Stack
- **FastAPI**: Main web framework
- **CrewAI**: Agent orchestration (Researcher & Analyst)
- **Supabase**: PostgreSQL Database with REST API
- **Ollama / HuggingFace**: LLM Providers

Ensure your Ollama local server is running `llama3.2` if you choose `LLM_PROVIDER=ollama`. 
Otherwise, configure `huggingface/mistralai/Mistral-7B-Instruct-v0.2` via `LLM_PROVIDER=huggingface`.
