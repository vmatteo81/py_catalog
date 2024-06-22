from fastapi import FastAPI, HTTPException, Query
from typing import Optional, Dict, Any

from models.CatalogsMock import CatalogsMock
from models.Prize import Prize  # Assumendo che Prize sia una classe pydantic.BaseModel

app = FastAPI()
db = CatalogsMock()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/catalogs/{catalog_id}/prizes", response_model=Dict[str, Any])
def list_prizes(
    catalog_id: int,
    filter_id: Optional[int] = Query(None, alias="filter.id"),
    filter_description: Optional[str] = Query(None, alias="filter.description"),
    page: int = Query(1, alias="pagination.page"),
    per_page: int = Query(10, alias="pagination.per_page")
):
    filter = {}
    if filter_id is not None:
        filter['id'] = filter_id
    if filter_description is not None:
        filter['description'] = filter_description
    
    # Gestione di Catalog Not Found
    catalog = next((cat for cat in db.catalogs if cat["catalog_id"] == catalog_id), None)
    if not catalog:
        raise HTTPException(status_code=404, detail="Catalog not found")

    try:
        result = db.get_prizes(catalog_id, filter, {"page": page, "per_page": per_page})
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return result
