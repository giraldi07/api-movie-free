from fastapi import FastAPI
from api.routes import movies, tvseries, genres, releases

app = FastAPI()

# Daftarkan rute
app.include_router(movies.router, prefix="/movies", tags=["Movies"])
app.include_router(tvseries.router, prefix="/tvseries", tags=["TV Series"])
app.include_router(genres.router, prefix="/genres", tags=["Genres"])
app.include_router(releases.router, prefix="/releases", tags=["Releases"])

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie API"}

