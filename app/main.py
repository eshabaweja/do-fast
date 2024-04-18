from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel 

app = FastAPI()

# notes = {
#     1: "Total stable flexibility",
#     2: "Horizontal content-based system engine",
#     3: "Self-enabling uniform emulation",
#     4: "Public-key bottom-line emulation",
#     5: "Secured dynamic superstructure",
#     6: "Cross-group explicit knowledge user",
#     7: "Expanded clear-thinking data-warehouse",
#     8: "Vision-oriented 4th generation leverage",
#     9: "Multi-lateral context-sensitive knowledge user",
#     10: "Universal optimal instruction set",
# }


@app.get("/")
async def root():
    return {"message": "Here's a notes app"}

@app.post("/note")
def create_note(payLoad: dict = Body(...)):
    print(payLoad)
    return {payLoad['id']:payLoad['node_text']}

@app.get("/note/{id}")
def read_note(id: int):
    return {id:notes[id]}

def update_note(id: int):
    pass
