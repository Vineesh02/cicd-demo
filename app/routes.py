from typing import List

from fastapi import APIRouter

router = APIRouter()

ITEMS = [
    {"id": 1, "name": "First item"},
    {"id": 2, "name": "Second item"},
]


@router.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@router.get("/items/{item_id}")
def read_item(item_id: int) -> dict:
    return {"item_id": item_id, "message": "CI/CD demo item"}


@router.get("/items", response_model=List[dict])
def list_items() -> List[dict]:
    return ITEMS

