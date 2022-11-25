from models.usuario import Usuario
from mongoengine import ValidationError


def insert_usuario(item):

    try:
        usuario = Usuario()
        usuario.FirstName = item.first_name
        usuario.LastName = item.last_name
        usuario.Email = item.email
        usuario.YearsPreviousExperience = item.years_previous_experience
        usuario.Skills = item.skills

        usuario.save()

        message = "Escritura de datos correcta"
        return True, 200, message

    except ValidationError as e:
        message = f"El campo {list(e.errors.keys())[0]} no es válido"
        return False, 400, message

    except Exception:
        message = "Error al escribir los datos"
        return False, 400, message


def get_usuario(skills):
    # pipeline = 
    try:
        usuario_results = Usuario.objects()
        print(usuario_results.to_mongo().to_dict())
        message = "Escritura de datos correcta"
        return True, 200, message

    except ValidationError as e:
        message = f"El campo {list(e.errors.keys())[0]} no es válido"
        return False, 400, message

    except Exception:
        message = "Error al escribir los datos"
        return False, 400, message


def update_usuario(item):
    nombre_usuario = item.get('first_name', '')
    apellido_usuario = item.get('last_name', '')
    try:
        usuario = Usuario.objects(FirstName=nombre_usuario,
                                  LastName=apellido_usuario).first()
        email = item.get('email', '')
        years_previous_experience = item.get('years_previous_experience', '')
        skills = item.get('skills', '')
        usuario.update(Email=email if email else usuario.Email,
                       YearsPreviousExperience=years_previous_experience if years_previous_experience else usuario.years_previous_experience, # noqa
                       Skills=skills if skills else usuario.skills,
                       )
        usuario.reload()
        print(usuario.to_mongo().to_dict())
        message = "Escritura de datos correcta"
        return True, 200, message

    except ValidationError as e:
        message = f"El campo {list(e.errors.keys())[0]} no es válido"
        return False, 400, message

    except Exception:
        message = "Error al escribir los datos"
        return False, 400, message


def delete_usuario(item):
    # pipeline = 
    nombre_usuario = item.first_name
    apellido_usuario = item.last_name
    try:
        if not nombre_usuario or not apellido_usuario:
            message = "se deben indicar los campos first_name y last_name"
            return False, 400, message
        usuario = Usuario.objects(FirstName=nombre_usuario,
                                  LastName=apellido_usuario).first()
        if not usuario:
            message = "No encontró el usuario"
            return True, 404, message
        print(usuario.to_mongo().to_dict())
        usuario.delete()
        message = "Escritura de datos correcta"
        return True, 200, message

    except ValidationError as e:
        message = f"El campo {list(e.errors.keys())[0]} no es válido"
        return False, 400, message

    except Exception as e:
        print(e)
        message = "Error al escribir los datos"
        return False, 400, message
