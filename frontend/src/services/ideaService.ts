import { Idea } from "@/types";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export const ideaService = {
  async generateIdeas(field: string, noveltyLevel: number): Promise<Idea[]> {
    const res = await fetch(`${API_BASE}/api/ideas/generate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ field, noveltyLevel }),
    });

    if (!res.ok) {
      throw new Error("Failed to generate ideas");
    }
    return res.json();
  },

  async getSavedIdeas(): Promise<Idea[]> {
    const res = await fetch(`${API_BASE}/api/dashboard/ideas`);
    if (!res.ok) {
      return [];
    }
    return res.json();
  },

  async saveIdea(idea: Idea): Promise<void> {
    await fetch(`${API_BASE}/api/dashboard/ideas`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(idea),
    });
  },

  async deleteIdea(id: string): Promise<void> {
    await fetch(`${API_BASE}/api/dashboard/ideas/${id}`, { method: "DELETE" });
  },
};
