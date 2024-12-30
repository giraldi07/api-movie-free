from fastapi import APIRouter, HTTPException
import pandas as pd
from api.models import Movie

# movie_router = APIRouter()
router = APIRouter()

# Load data
movies_file_path = "./data/movies.csv"
df_movies = pd.read_csv(movies_file_path)

# Pastikan release_date diubah menjadi format datetime
df_movies.rename(columns={'data 2': 'release_date'}, inplace=True)
df_movies['release_date'] = pd.to_datetime(df_movies['release_date'], errors='coerce')

movies = df_movies.to_dict(orient="records")

@router.get("/")
def get_movies():
    return {"movies": movies}

# ------------------- Tambahan untuk Search -------------------

@router.get("/search")
def search_movies(title: str):
    """
    Cari film berdasarkan judul.
    """
    if not title:
        raise HTTPException(status_code=400, detail="Query parameter is required.")
    
    # Filter film berdasarkan judul yang mengandung title
    search_result = df_movies[df_movies['data'].str.contains(title, case=False, na=False)]
    
    if search_result.empty:
        raise HTTPException(status_code=404, detail="No movies found matching the query.")
    
    return {"search_results": search_result.to_dict(orient="records")}



# ------------------- Tambahan untuk Group by Year -------------------

@router.get("/grouped_by_year")
def get_movies_grouped_by_year():
    """
    Kelompokkan film berdasarkan tahun rilis.
    """
    if 'release_date' not in df_movies or df_movies['release_date'].isnull().all():
        raise HTTPException(status_code=404, detail="No valid release_date found.")
    
    df_movies['year'] = df_movies['release_date'].dt.year
    grouped_movies = (
        df_movies.dropna(subset=['year'])
        .groupby('year')
        .apply(lambda x: x.to_dict(orient='records'))
        .to_dict()
    )
    return {"movies_by_year": grouped_movies}


# ------------------- Tambahan untuk Group by Rating -------------------

@router.get("/grouped_by_rating")
def get_movies_grouped_by_rating():
    """
    Kelompokkan film berdasarkan kelompok rating.
    """
    if 'rating' not in df_movies or df_movies['rating'].isnull().all():
        raise HTTPException(status_code=404, detail="No valid rating found.")
    
    # Tentukan rentang rating
    bins = [0, 2, 4, 6, 8, 10]
    labels = ["0-2", "2-4", "4-6", "6-8", "8-10"]
    df_movies['rating_group'] = pd.cut(df_movies['rating'], bins=bins, labels=labels, include_lowest=True)

    # Kelompokkan film berdasarkan kelompok rating
    grouped_movies = (
        df_movies.groupby('rating_group')
        .apply(lambda x: x.to_dict(orient='records'))
        .to_dict()
    )
    return {"movies_by_rating": grouped_movies}


@router.get("/{movie_id}")
def get_movie(movie_id: int):
    if 0 <= movie_id < len(movies):
        return {"movie": movies[movie_id]}
    raise HTTPException(status_code=404, detail="Movie not found")

@router.post("/")
def add_movie(movie: Movie):
    new_movie = movie.dict()
    movies.append(new_movie)
    return {"message": "Movie added successfully", "movie": new_movie}

@router.put("/{movie_id}")
def update_movie(movie_id: int, movie: Movie):
    if 0 <= movie_id < len(movies):
        movies[movie_id] = movie.dict()
        return {"message": "Movie updated successfully", "movie": movies[movie_id]}
    raise HTTPException(status_code=404, detail="Movie not found")

@router.delete("/{movie_id}")
def delete_movie(movie_id: int):
    if 0 <= movie_id < len(movies):
        deleted_movie = movies.pop(movie_id)
        return {"message": "Movie deleted successfully", "movie": deleted_movie}
    raise HTTPException(status_code=404, detail="Movie not found")


