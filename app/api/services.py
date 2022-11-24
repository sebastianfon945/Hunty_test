from models.vacante import Vacante
from mongoengine import ValidationError


def insert_vacante(item):

    try:
        vacante = Vacante()
        vacante.PositionName = item.position_name
        vacante.CompanyName = item.company_name
        vacante.Salary = item.salary
        vacante.Currency = item.currency
        vacante.VacancyLink = item.vacancy_link
        vacante.RequiredSkills = item.required_skills

        vacante.save()

        message = "Escritura de datos correcta"
        return True, 200, message

    except ValidationError as e:
        message = f"El campo {list(e.errors.keys())[0]} no es válido"
        return False, 400, message

    except Exception:
        message = "Error al escribir los datos"
        return False, 400, message


def get_vacante(skills):

    try:
        vacante_results = Vacante.objects().first()
        print(vacante_results.to_mongo().to_dict())
        message = "Escritura de datos correcta"
        return True, 200, message

    except ValidationError as e:
        message = f"El campo {list(e.errors.keys())[0]} no es válido"
        return False, 400, message

    except Exception:
        message = "Error al escribir los datos"
        return False, 400, message
