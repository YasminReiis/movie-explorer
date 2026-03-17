from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Movie Explorer API")

# Permitir que o frontend acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de filme
class Movie(BaseModel):
    title: str
    year: int
    genre: str
    image_url: str
    description: Optional[str] = None

movies: List[Movie] = []

# Rota raiz
@app.get("/")
def root():
    return {"message": "Movie Explorer API running"}

# Listar todos os filmes
@app.get("/movies")
def get_movies():
    return movies

# Adicionar filme
@app.post("/movies")
def create_movie(movie: Movie):
    movies.append(movie)
    return {"message": "Movie added", "movie": movie}

# Pegar um filme por ID
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    if movie_id >= len(movies):
        raise HTTPException(status_code=404, detail="Movie not found")
    return movies[movie_id]

# Atualizar filme
@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: Movie):
    if movie_id >= len(movies):
        raise HTTPException(status_code=404, detail="Movie not found")
    movies[movie_id] = movie
    return {"message": "Movie updated"}

# Deletar filme
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    if movie_id >= len(movies):
        raise HTTPException(status_code=404, detail="Movie not found")
    movies.pop(movie_id)
    return {"message": "Movie deleted"}

# Recomendação aleatória
@app.get("/recommend")
def recommend_movie():
    import random
    if not movies:
        raise HTTPException(status_code=404, detail="No movies available")
    return random.choice(movies)
