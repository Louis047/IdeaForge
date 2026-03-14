import { Expert } from "@/types";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export const expertService = {
  async getExperts(field?: string): Promise<Expert[]> {
    const params = field ? `?field=${field}` : "";
    const res = await fetch(`${API_BASE}/api/experts${params}`);
    if (!res.ok) return [];
    return res.json();
  },
};
