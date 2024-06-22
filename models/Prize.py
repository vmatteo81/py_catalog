from pydantic import BaseModel

class Prize(BaseModel):
    id: int
    title: str
    description: str
    image: str