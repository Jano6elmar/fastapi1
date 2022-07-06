from fastapi import APIRouter
from app.schemas import User, UserId

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)
usuarios = []


@router.get('/ruta1')
def ruta1():
    return {"mensaje": "Bienvenido a tu primera api"}

@router.get('/')
def obtener_usuario():
    return usuarios

@router.post('/')
def crear_usuario(user:User):
    usuario = user.dict()
    usuarios.append(usuario)
    return {"respuesta": "Usuario creado satisfactoriamente!"}

@router.get('/{user_id}')
def obtener_usuario(user_id:int):
    for user in usuarios:
        if user["id"] == user_id:
            return {"usuario":user}
    return {"respuesta": "usuario no encontrado!!"}

@router.post('/obtener_usuario')
def obtener_usuario_2(user_id:UserId):
    for user in usuarios:
        if user["id"] == user_id.id:
            return {"usuario":user}
    return {"respuesta": "usuario no encontrado!!"}

@router.delete('/')
def eliminar_usuario(user_id:int):
    for index, user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios.pop(index)
            return {"respuesta": "Usuario eliminado correctamente!"}
    return {"respuesta": "usuario no encontrado!!"}

@router.put('/{user_id}')
def actualizar_user(user_id:int, updateUser:User):
    for index, user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios[index]["title"]= updateUser.dict()["title"]
            usuarios[index]["content"]= updateUser.dict()["content"]
            usuarios[index]["author"]= updateUser.dict()["auhtor"]
            return {"respuesta": "Usuario actualizado correctamente!"}
    return {"respuesta":"usuario no encontrado!!"}
