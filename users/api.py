from ninja import Router
from .schemas import UserSchema, TypeUserSchema
from django.contrib.auth.hashers import make_password
from .models import User
from django.core.exceptions import ValidationError
from rolepermissions.roles import assign_role

users_router = Router()

@users_router.post("new", response={201: dict, 400: dict, 500: dict})
def create_user(request, type_user_schema:TypeUserSchema):
    user = User(**type_user_schema.user.dict())
    user.password = make_password(type_user_schema.user.password)
   
    try:
       user.full_clean()  # Validate the user data
       user.save()
       assign_role(user, type_user_schema.type_user.type)
    except ValidationError as e:
       return 400, {"error": str(e)}

    return 201, {"user_id": user.id}