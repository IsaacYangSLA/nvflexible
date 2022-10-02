from typing import Union
from datetime import datetime

from pydantic import BaseModel

class Dummy(BaseModel):
    id : int
    random_string : str

    class Config:
        orm_mode = True


"""
class SubmissionCustomField(BaseModel):
    id : int
    key_name : str
    value_type : str
    value_string : str


class SubmissionBase(BaseModel):
    state : str = ""
    custom_fields : list[SubmissionCustomField] = []

class SubmissionCreate(SubmissionBase):
    parents : list['Submission']

    class Config:
        orm_mode = True


class Submission(SubmissionBase):
    id: int
    owner_id: int
    parents : list['Submission']
    created_at : datetime
    updated_at : datetime
    class Config:
        orm_mode = True


class ParticipantBase(BaseModel):
    email: str


class ParticipantCreate(ParticipantBase):
    pass

class Participant(ParticipantBase):
    id : int
    project_id : int
    submission_ids: list[int] = []

    class Config:
        orm_mode = True

class VitalSignCreate(BaseModel):
    participant_id : int
    custom_fields : dict[str, object] = dict()

    class Config:
        orm_mode = True

class VitalSign(VitalSignCreate):
    id : int
    custom_fields : dict[str, object] = dict()

    class Config:
        orm_mode = True
"""