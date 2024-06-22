import pytest
from models.CatalogsMock import CatalogsMock

db = CatalogsMock()

def test_get_prizes_no_filters():
    result = db.get_prizes(1)
    assert result["total"] == 0

def test_get_prizes_with_id_filter():
    result = db.get_prizes(3, filter={"id": 3})
    assert result["total"] == 1
    assert result["prizes"][0].id == 3

def test_get_prizes_with_description_filter():
    result = db.get_prizes(4, filter={"description": "prize"})
    assert result["total"] == 10
    assert all("prize" in prize.description.lower() for prize in result["prizes"])

def test_get_prizes_pagination():
    result = db.get_prizes(5, pagination={"page": 2, "per_page": 10})
    assert result["total"] == 10
    assert result["prizes"][0].id == 11

def test_get_prizes_invalid_catalog_id():
    with pytest.raises(ValueError) as excinfo:
        db.get_prizes(10)
    
    assert "Catalog not found" in str(excinfo.value)

def test_get_prizes_empty_catalog():
    result = db.get_prizes(1)
    assert result["total"] == 0

def test_get_prizes_invalid_pagination():
    result = db.get_prizes(3, pagination={"page": 10, "per_page": 10})
    assert result["total"] == 0

def test_get_prizes_no_results():
    result = db.get_prizes(2, filter={"id": 2, "description": "not existing"})
    assert result["total"] == 0

def test_get_prizes_multiple_filters():
    result = db.get_prizes(4, filter={"id": 4, "description": "prize"})
    assert result["total"] == 1
    assert result["prizes"][0].id == 4

def test_get_prizes_no_pagination():
    result = db.get_prizes(5)
    assert result["total"] == 50
