from typing import Union
from xmlrpc.client import DateTime

from pydantic import BaseModel

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
    created_at : DateTime
    updated_at : DateTime
    class Config:
        orm_mode = True


class ParticipantBase(BaseModel):
    email: str


class ParticipantCreate(ParticipantBase):
    password: str


class Participant(ParticipantBase):
    id: int
    is_active: bool
    items: list[Submission] = []

    class Config:
        orm_mode = True