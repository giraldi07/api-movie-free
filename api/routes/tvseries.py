from fastapi import APIRouter, HTTPException
import pandas as pd
from api.models import TVSeries

router = APIRouter()

tvseries_file_path = "./data/tvseries.csv"
df_tvseries = pd.read_csv(tvseries_file_path)

@router.get("/")
def get_tvseries():
    return {"tvseries": df_tvseries.to_dict(orient="records")}


@router.get("/search")
def search_tvseries(title: str):
    """
    Cari TV series berdasarkan judul.
    """
    if not title:
        raise HTTPException(status_code=400, detail="Query parameter 'title' is required.")
    
    # Filter TV series berdasarkan judul yang mengandung title
    search_result = df_tvseries[df_tvseries['data'].str.contains(title, case=False, na=False)]
    
    if search_result.empty:
        raise HTTPException(status_code=404, detail="No TV series found matching the query.")
    
    return {"search_results": search_result.to_dict(orient="records")}



@router.get("/{tvseries_id}")
def get_tvseries_by_id(tvseries_id: int):
    if 0 <= tvseries_id < len(df_tvseries):
        return {"tvseries": df_tvseries.iloc[tvseries_id].to_dict()}
    raise HTTPException(status_code=404, detail="TV series not found")

@router.post("/")
def add_tvseries(tvseries: TVSeries):
    new_tvseries = tvseries.dict()
    df_new_row = pd.DataFrame([new_tvseries])
    global df_tvseries
    df_tvseries = pd.concat([df_tvseries, df_new_row], ignore_index=True)
    return {"message": "TV series added successfully", "tvseries": new_tvseries}

@router.delete("/{tvseries_id}")
def delete_tvseries(tvseries_id: int):
    global df_tvseries
    if 0 <= tvseries_id < len(df_tvseries):
        deleted_tvseries = df_tvseries.iloc[tvseries_id].to_dict()
        df_tvseries = df_tvseries.drop(index=tvseries_id).reset_index(drop=True)
        return {"message": "TV series deleted successfully", "tvseries": deleted_tvseries}
    raise HTTPException(status_code=404, detail="TV series not found")
