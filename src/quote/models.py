from pydantic import BaseModel


class Quote(BaseModel):
    id: int
    category: int
    source: int
    content: str
