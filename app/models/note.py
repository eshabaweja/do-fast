# model definition for notes
from typing import Optional
from pydantic import BaseModel 

class Note(BaseModel):
    id: int
    note_title: str = ""
    note_text: Optional[str] = None