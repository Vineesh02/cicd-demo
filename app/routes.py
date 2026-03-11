from typing import Dict, List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ItemCreate(BaseModel):
    name: str


ITEMS: List[Dict] = [
    {"id": 1, "name": "First item"},
    {"id": 2, "name": "Second item"},
]


@router.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@router.get("/items/{item_id}")
def read_item(item_id: int) -> dict:
    return {"item_id": item_id, "message": "CI/CD demo item"}


@router.get("/items", response_model=List[Dict])
def list_items() -> List[Dict]:
    return ITEMS


@router.post("/items", response_model=Dict)
def create_item(payload: ItemCreate) -> Dict:
    new_id = max(item["id"] for item in ITEMS) + 1 if ITEMS else 1
    item = {"id": new_id, "name": payload.name}
    ITEMS.append(item)
    return item

