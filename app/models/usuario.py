import uuid
from mongoengine import Document, StringField, IntField, ListField, EmailField


class Vacante(Document):
    UserId = uuid.uuid4()
    FirstName = StringField()
    LastName = StringField()
    Email = EmailField()
    YearsPreviousExperience = IntField()  
    Skills = ListField(default=[])

