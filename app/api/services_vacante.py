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
    # pipeline = 
    try:
        vacante_results = Vacante.objects()
        print(vacante_results.to_mongo().to_dict())
        message = "Escritura de datos correcta"
        return True, 200, message

    except ValidationError as e:
        message = f"El campo {list(e.errors.keys())[0]} no es válido"
        return False, 400, message

    except Exception:
        message = "Error al escribir los datos"
        return False, 400, message


def update_vacante(item):
    nombre_vacante = item.get('position_name', '')
    nombre_empresa = item.get('company_name', '')
    try:
        vacante = Vacante.objects(PositionName=nombre_vacante,
                                  CompanyName=nombre_empresa).first()
        salary = item.get('salary', '')
        currency = item.get('currency', '')
        required_skills = item.get('required_skills', '')
        vacante.update(Salary=salary if salary else vacante.Salary,
                       Currency=currency if currency else vacante.Currency,
                       RequiredSkills=required_skills if required_skills else vacante.RequiredSkills, # noqa
                       )
        vacante.reload()
        print(vacante.to_mongo().to_dict())
        message = "Escritura de datos correcta"
        return True, 200, message

    except ValidationError as e:
        message = f"El campo {list(e.errors.keys())[0]} no es válido"
        return False, 400, message

    except Exception:
        message = "Error al escribir los datos"
        return False, 400, message


def delete_vacante(item):
    # pipeline = 
    nombre_vacante = item.position_name
    nombre_empresa = item.company_name
    try:
        if not nombre_vacante or not nombre_empresa:
            message = "se deben indicar los campos position_name y company_name"
            return False, 400, message
        vacante = Vacante.objects(PositionName=nombre_vacante,
                                  CompanyName=nombre_empresa).first()
        print(vacante.to_mongo().to_dict())
        vacante.delete()
        message = "Escritura de datos correcta"
        return True, 200, message

    except ValidationError as e:
        message = f"El campo {list(e.errors.keys())[0]} no es válido"
        return False, 400, message

    except Exception:
        message = "Error al escribir los datos"
        return False, 400, message
