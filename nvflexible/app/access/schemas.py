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


class Participant(CommonMixin, Base):
    __tablename__ = "participants"

    cert_id = Column(Integer, ForeignKey("certificate.id"), nullable=False)
    certificate = relationship("Certificate", lazy=True, uselist=False)
    vital_signs = relationship("VitalSign", lazy=True, backref=backref("participant", uselist=False))
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)
    submissions = relationship("Submission", lazy=True, backref=backref("participant", uselist=False))

    def asdict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


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
    custom_fields : dict(str, object) = dict()

    class Config:
        orm_mode = True

class VitalSign(VitalSignCreate):
    id : int
    custom_fields : dict(str, object) = dict()

    class Config:
        orm_mode = True