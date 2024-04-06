from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from movie import Movie

# To run do `uvicorn main:app --reload`

app = FastAPI()
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "world"}

movies = []
mov_count = 0
with open("./movies.txt", 'r', encoding="utf-8") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        
        if i % 3 == 0:
            mov = Movie(
                id=mov_count,
                name=line.strip(),
                cast=lines[i+1].strip().split(", ")
            )
            movies.append(mov)
            mov_count += 1

    print("hiu")
            
    mov_count += 1

for mov in movies:
    print(mov.id)
    print(mov.name)
    print(mov.cast)
    print()