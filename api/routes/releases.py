from fastapi import APIRouter, HTTPException
import pandas as pd
from api.models import Release

router = APIRouter()

release_file_path = "./data/release.csv"
df_releases = pd.read_csv(release_file_path)

@router.get("/")
def get_releases():
    return {"releases": df_releases.to_dict(orient="records")}

@router.get("/{release_id}")
def get_release(release_id: int):
    if 0 <= release_id < len(df_releases):
        return {"release": df_releases.iloc[release_id].to_dict()}
    raise HTTPException(status_code=404, detail="Release not found")

@router.post("/")
def add_release(release: Release):
    new_release = release.dict()
    df_new_row = pd.DataFrame([new_release])
    global df_releases
    df_releases = pd.concat([df_releases, df_new_row], ignore_index=True)
    return {"message": "Release added successfully", "release": new_release}

@router.delete("/{release_id}")
def delete_release(release_id: int):
    global df_releases
    if 0 <= release_id < len(df_releases):
        deleted_release = df_releases.iloc[release_id].to_dict()
        df_releases = df_releases.drop(index=release_id).reset_index(drop=True)
        return {"message": "Release deleted successfully", "release": deleted_release}
    raise HTTPException(status_code=404, detail="Release not found")
