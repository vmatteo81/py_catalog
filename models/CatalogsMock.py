from typing import Dict, Any, Optional
from models.Prize import Prize  # Assumendo che Prize sia una classe pydantic.BaseModel

class CatalogsMock:
    def __init__(self):
        self.catalogs = [
            {
                "catalog_id": 1,
                "prizes": []
            },
            {
                "catalog_id": 2,
                "prizes": [
                    Prize(id=1, title="Prize 1", description="Description of prize 1", image="https://www.mycatalog.it/img/image1.png")
                ]
            },
            {
                "catalog_id": 3,
                "prizes": [
                    Prize(id=i, title=f"Prize {i}", description=f"Description of prize {i}", image=f"https://www.mycatalog.it/img/image{i}.png")
                    for i in range(1, 6)
                ]
            },
            {
                "catalog_id": 4,
                "prizes": [
                    Prize(id=i, title=f"Prize {i}", description=f"Description of prize {i}", image=f"https://www.mycatalog.it/img/image{i}.png")
                    for i in range(1, 11)
                ]
            },
            {
                "catalog_id": 5,
                "prizes": [
                    Prize(id=i, title=f"Prize {i}", description=f"Description of prize {i}", image=f"https://www.mycatalog.it/img/image{i}.png")
                    for i in range(1, 51)
                ]
            }
        ]
    
    def get_prizes(self, catalog_id: int, filter: Optional[Dict[str, Any]] = None, pagination: Optional[Dict[str, int]] = None) -> Dict[str, Any]:
        catalog = next((cat for cat in self.catalogs if cat["catalog_id"] == catalog_id), None)
        if not catalog:
            raise ValueError("Catalog not found")
        
        prizes = catalog["prizes"]
        
        if filter:
            if 'id' in filter:
                prizes = [prize for prize in prizes if prize.id == filter['id']]
            if 'description' in filter:
                prizes = [prize for prize in prizes if filter['description'].lower() in prize.description.lower()]

        total = len(prizes)
        
        if pagination:
            page = pagination.get('page', 1)
            per_page = pagination.get('per_page', 10)
            start = (page - 1) * per_page
            end = start + per_page
            prizes = prizes[start:end]
            total = len(prizes)
        
        return {"total": total, "prizes": prizes}
