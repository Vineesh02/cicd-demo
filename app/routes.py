from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@router.get("/items/{item_id}")
def read_item(item_id: int) -> dict:
    return {"item_id": item_id, "message": "CI/CD demo item"}

