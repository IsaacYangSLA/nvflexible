from typing import Union

from pydantic import BaseModel


class SubmissionBase(BaseModel):
    state : str = ""


class SubmissionCreate(SubmissionBase):
    pass


class Submission(SubmissionBase):
    id: int
    owner_id: int

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