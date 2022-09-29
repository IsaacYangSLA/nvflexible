from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")

async def get_mandatory_headers(headers):
    project = headers.get("X-Project")
    if not project:
        return None
    study = headers.get("X-Study")
    if not study:
        return None
    pct = headers.get("X-Pct")
    if not pct:
        return None
    return (project, study, pct)

