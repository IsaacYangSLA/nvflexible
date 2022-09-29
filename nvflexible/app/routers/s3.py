from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/persist",
    tags=["persist"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def persist_done():
    req = request.json
    blob_id = req.get("Key").split("/")[1]
    SubmissionManager.update_state(blob_id, "uploaded")
    return jsonify({"status": "success"})
