# model definition for notes
import uuid
from pydantic import BaseModel

class Note(BaseModel):
    id: str = ""
    note_title: str = ""
    note_text: str = ""