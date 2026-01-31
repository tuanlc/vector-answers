from asyncio.log import logger
import json
import re
from pydantic import BaseModel
import google.generativeai as genai
from config import GEMINI_API_KEY

class RewriteRequest(BaseModel):
    text: str

class RewriteResponse(BaseModel):
    intent: str
    refined_query: str

class RewriteProvider:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
            
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.system_prompt = self._load_system_prompt()

    def _load_system_prompt(self) -> str:
        with open("prompts/rewrite_system.md", "r", encoding="utf-8") as f:
                return f.read().strip()

    def rewrite(self, text: str) -> RewriteResponse:
        """Rewrite a user query into a structured format"""
        try:
            # Construct the full prompt
            full_prompt = f"{self.system_prompt}\n\nUser Query: {text}\n\nResponse (JSON only):"
            
            response = self.model.generate_content(full_prompt)
            raw = response.text
            match = re.search(r"\{.*\}", raw, re.S)
            if match:
                data = json.loads(match[0])
                return RewriteResponse(
                    intent=data.get("intent", "general"),
                    refined_query=data.get("refined_query", text)
                )
            else:
                logger.error("No JSON object found in the response")
                return RewriteResponse(
                    intent="general",
                    refined_query=text
                )
        except Exception as e:
            logger.error(f"Error in rewrite_query: {e}")
            # Fallback response
            return RewriteResponse(
                intent="general",
                refined_query=text
            )