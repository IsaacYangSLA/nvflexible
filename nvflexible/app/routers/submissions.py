from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_mandatory_headers

router = APIRouter(
    prefix="/submissions",
    tags=["submissions"],
    dependencies=[Depends(get_mandatory_headers)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_submissions():
    key_tuple = get_mandatory_headers(request.header)
    if not key_tuple:
        return jsonify({"status": "error"})
    if request.method == "GET":
        return jsonify({"status": "success", "submission_list": SubmissionManager.get_all(*key_tuple)})
    req = request.json
    result = SubmissionManager.store_new_entry(*key_tuple, **req)
    if result is None:
        return jsonify({"status": "error"})
    return jsonify({"status": "success", "submission": result})


@router.post("/")
def add_submission():
    key_tuple = get_mandatory_headers(request.header)
    if not key_tuple:
        return jsonify({"status": "error"})
    if request.method == "GET":
        return jsonify({"status": "success", "submission_list": SubmissionManager.get_all(*key_tuple)})
    req = request.json
    result = SubmissionManager.store_new_entry(*key_tuple, **req)
    if result is None:
        return jsonify({"status": "error"})
    return jsonify({"status": "success", "submission": result})


@router.get("/{sub_id}/custom_fields")
def read_custom_fields(sub_id):
    custom_field = SubmissionManager.get_custom_field(sub_id)
    return jsonify({"status": "success", "custom_field": custom_field})


@router.get("/{sub_id}/parents")
def read_parents(sub_id):
    parent_list = SubmissionManager.get_parents(sub_id)
    return jsonify({"status": "success", "parent_list": parent_list})


@router.get("/{sub_id}/children")
def read_children(sub_id):
    child_list = SubmissionManager.get_children(sub_id)
    return jsonify({"status": "success", "child_list": child_list})


@router.get("/root")
def read_root():
    req = request.json
    result = SubmissionManager.get_root(**req)
    if result is None:
        return jsonify({"status": "error"})
    return jsonify({"status": "success", "submission": result})


