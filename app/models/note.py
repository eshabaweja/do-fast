# model definition for notes
import uuid
from pydantic import BaseModel, UUID4

class Note(BaseModel):
    id: UUID4 = uuid.uuid4()
    note_title: str = ""
    note_text: str = ""