from fastapi import APIRouter, HTTPException
import pandas as pd
from api.models import Genre

router = APIRouter()

genre_file_path = "./data/genre.csv"
df_genres = pd.read_csv(genre_file_path)

@router.get("/")
def get_genres():
    return {"genres": df_genres.to_dict(orient="records")}

@router.get("/{genre_id}")
def get_genre(genre_id: int):
    if 0 <= genre_id < len(df_genres):
        return {"genre": df_genres.iloc[genre_id].to_dict()}
    raise HTTPException(status_code=404, detail="Genre not found")

@router.post("/")
def add_genre(genre: Genre):
    new_genre = genre.dict()
    df_new_row = pd.DataFrame([new_genre])
    global df_genres
    df_genres = pd.concat([df_genres, df_new_row], ignore_index=True)
    return {"message": "Genre added successfully", "genre": new_genre}

@router.delete("/{genre_id}")
def delete_genre(genre_id: int):
    global df_genres
    if 0 <= genre_id < len(df_genres):
        deleted_genre = df_genres.iloc[genre_id].to_dict()
        df_genres = df_genres.drop(index=genre_id).reset_index(drop=True)
        return {"message": "Genre deleted successfully", "genre": deleted_genre}
    raise HTTPException(status_code=404, detail="Genre not found")
