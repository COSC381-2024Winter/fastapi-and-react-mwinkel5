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
            
    mov_count += 1

@app.get("/movie/{movie_id}")
def get_movie(movie_id: int):
    for i, mov in enumerate(movies):
        if mov.id == movie_id:
            return {
                "id": mov.id,
                "name": mov.name,
                "cast": mov.cast
            }
    return None