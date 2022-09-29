from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/health",
    tags=["health"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/vital_sign")
async def add_vital_sign():
    headers = request.headers
    project = headers.get("X-Project")
    if not project:
        return jsonify({"status": "error"})
    study = headers.get("X-Study")
    if not study:
        return jsonify({"status": "error"})
    pct = headers.get("X-Pct")
    if not pct:
        return jsonify({"status": "error"})
    req = request.json
    key_tuple = (
        project,
        study,
        pct,
    )
    result = VitalSignManager.insert_entry(*key_tuple, **req)
    if result is None:
        return jsonify({"status": "error"})
    exp = ExpAdm.get_current_exp(study, pct)
    result = PlanAdm.get_current_plan(exp.name, study_name=study, project_name=project)
    if result is None:
        return jsonify({"status": "error", "plan": None})
    return jsonify({"status": "success", "plan": result})


