from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/provision")
async def provision():
    req = request.json
    issuer = req.pop("issuer", None)
    subject = req.pop("subject", "")
    result = CertManager.store_new_entry(issuer, subject, **req)
    if result is None:
        return jsonify({"status": "error"})
    return jsonify(
        {
            "status": "success",
            "certificate": {"cert": result.s_crt.decode("utf-8"), "key": result.s_prv.decode("utf-8")},
        }
    )

@router.get("/refresh")
async def refresh():
    SystemManager.init_backend()
    return jsonify({"status": "success"})


@router.post("/plan")
async def add_plan():
    req = request.json
    result = PlanManager.store_new_entry(**req)
    if result is None:
        return jsonify({"status": "error"})
    return jsonify({"status": "success", "plan": result})

@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}

   
@router.post("/study")
async def add_study():
    headers = request.headers
    project = headers.get("X-Project")
    if not project:
        return jsonify({"status": "error"})
    req = request.json
    result = StudyManager.new_entry(project=project, **req)
    if result is None:
        return jsonify({"status": "error"})
    return jsonify({"status": "success", "study": result})


@router.post("/seed")
async def seed():
    req = request.json
    project = req.get("project")
    study = req.get("study")
    participants = req.get("participants")
    result = SeedManager.store_new_entry(project=project, study=study, participants=participants)
    if result is None:
        return jsonify({"status": "error"})
    return jsonify({"status": "success", "project": result})


