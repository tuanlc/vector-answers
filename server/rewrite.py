from pydantic import BaseModel

class RewriteRequest(BaseModel):
    text: str

class RewriteResponse(BaseModel):
    intent: str
    query: str

class RewriteProvider:
    def rewrite(self, text: str) -> RewriteResponse:
        return RewriteResponse(intent="example_intent", query=text[::-1])