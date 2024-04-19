from fastapi import FastAPI
from fastapi.params import Body
from models.note import Note
import uuid

app = FastAPI()

my_notes = []


@app.get("/")
async def root():
    return {"message": "Here's a notes app"}

@app.get("/notes")
def read_notes():
    return {"data": my_notes}

@app.post("/notes")
def create_note(note: Note):
    note.id=str(uuid.uuid4())
    note_dict = note.dict()
    my_notes.append(note_dict)
    return {"note":note_dict}

@app.get("/notes/{id}")
def read_note(id: str):
    print(id)
    for note_dict in my_notes:
        if note_dict["id"] == id:
            return note_dict
    return {"error":"Note does not exist."}

@app.put("/notes/{id}")
def update_note(id: str):
    pass

@app.delete("/notes/{id}")
def delete_note(id: str):
    pass

# if __name__ == "__main__":
#     note = Note(id=12)
#     print(note)