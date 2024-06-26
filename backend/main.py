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

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    if movie_id >= len(movies) or movie_id < 0 or not movies[movie_id]:
        return None
    mov = movies[movie_id]
    return {
        "name": mov.name,
        "cast": mov.cast
    }

@app.put("/movies/{movie_id}")
def put_movie(movie_id: int, movie: Movie):
    if movie_id >= len(movies) or movie_id < 0 or not movies[movie_id]:
        return None
    mov = movies[movie_id]
    mov.name = movie.name
    mov.cast = movie.cast
    return get_movie(movie_id)

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    if movie_id >= len(movies) or movie_id < 0 or not movies[movie_id]:
        return None
    mov = get_movie(movie_id)
    movies[movie_id] = None
    return mov

@app.post("/movies/add")
def post_movie(movie: Movie):
    for i, mov in enumerate(movies):
        if mov == None:
            # This will add the new movie in a space where a previous entry was deleted, to save space
            movies[i] = movie
            return i
    # This will just add the movie to the end if no movies have been deleted
    movies.append(movie)
    return len(movies)