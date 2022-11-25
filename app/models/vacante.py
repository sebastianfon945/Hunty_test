import uuid
from mongoengine import Document, StringField, IntField, ListField


class Vacante(Document):
    PositionName = StringField(required=True)
    CompanyName = StringField(required=True)
    Salary = IntField(required=True)
    Currency = StringField(required=True)
    VacancyId = uuid.uuid4()
    VacancyLink = StringField(required=True)
    RequiredSkills = ListField(default=[], required=True)
