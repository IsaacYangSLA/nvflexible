from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..access import crud, schemas

from ..dependencies import get_mandatory_headers, get_db

router = APIRouter(
    prefix="/dummy",
    tags=["dummy"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[schemas.Dummy])
def read_dummies(db: Session=Depends(get_db)):
    return crud.get_dummy(db)

@router.post("/", response_model=schemas.Dummy)
def create_dummy(db: Session=Depends(get_db)):
    item = crud.create_dummy(db)
    return item
    

    # key_tuple = get_mandatory_headers(request.header)
    # if not key_tuple:
    #     return jsonify({"status": "error"})
    # if request.method == "GET":
    #     return jsonify({"status": "success", "submission_list": SubmissionManager.get_all(*key_tuple)})
    # req = request.json
    # result = SubmissionManager.store_new_entry(*key_tuple, **req)
    # if result is None:
    #     return jsonify({"status": "error"})
    # return jsonify({"status": "success", "submission": result})

