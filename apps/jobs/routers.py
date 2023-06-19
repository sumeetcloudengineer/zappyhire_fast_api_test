from fastapi import APIRouter, Request, status, Response

router = APIRouter()


@router.get('/hello_world/', status_code=status.HTTP_200_OK)
def hello_world(name: str):
    return {'out': 'Hello ' + name}
