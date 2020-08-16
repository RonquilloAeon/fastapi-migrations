from pydantic import BaseModel


class Quote(BaseModel):
    id: int
    source: int
    content: str
