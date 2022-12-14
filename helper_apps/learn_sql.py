from datetime import datetime
import uuid
from nvflexible.application import create_app, db

app = create_app("development")
app.app_context().push()

from nvflexible.application.models import (
    Certificate,
    Experiment,
    Participant,
    Plan,
    Project,
    Study,
    Submission,
    SubmissionCustomField,
    VitalSign,
    VitalSignCustomField,
)

from nvflexible.application.managers import (
    CertAdm,
    PlanAdm,
    StudyAdm,
    ExpAdm,
    SubmissionManager,
    SystemManager,
    VitalSignManager,
)


def init():
    db.drop_all()
    db.create_all()

    fake_cert = Certificate()
    db.session.add(fake_cert)
    db.session.flush()
    p1 = Project(name="proj1", cert_id=fake_cert.id)
    db.session.add(p1)
    db.session.flush()

    s1 = Study(name="study1", project_id=p1.id)
    db.session.add(s1)
    db.session.flush()

    pct1 = Participant(name="site1", cert_id=fake_cert.id)
    pct1.project_id = p1.id
    pct1.study_id = s1.id
    db.session.add(pct1)
    db.session.flush()

    pct2 = Participant(name="site2", cert_id=fake_cert.id)
    pct2.project_id = p1.id
    pct2.study_id = s1.id
    db.session.add(pct2)
    db.session.flush()


init()
e1 = ExpAdm.insert_entry("exp1", "study1", "proj1", **{"participants": {"site1": "aggregator"}})
db.session.add(e1)
db.session.flush()
key_tuple = ("proj1", "study1", "site1")
sub = SubmissionManager.insert_entry("exp1", *key_tuple)
print(sub.id)
sub = SubmissionManager.insert_entry("exp1", *key_tuple, parent_id_list=[sub.id])
root_sub = SubmissionManager.get_root("exp1", *key_tuple)
print(root_sub)

plan = PlanAdm.insert_entry("plan1", "exp1", "study1", "proj1", **{"effective_time": "2022-04-08", "action": "wait"})
print(plan)

vital_sign_reply = VitalSignManager.insert_entry(*key_tuple, **{"status": "very happy"})
result = PlanAdm.get_current_plan(e1.name, study_name="study1", project_name="proj1")
print(result.asdict())
