import { Idea } from "@/types";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export const dashboardService = {
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

  async removeIdea(id: string): Promise<void> {
    await fetch(`${API_BASE}/api/dashboard/ideas/${id}`, { method: "DELETE" });
  },
};
