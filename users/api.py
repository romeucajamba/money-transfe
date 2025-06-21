from ninja import Router
from .schemas import UserSchema
from django.contrib.auth.hashers import make_password
from .models import User

users_router = Router()

@users_router.post("new", response={201: dict, 400: dict, 500: dict})
def create_user(request, user:UserSchema):
    user = User(**user.dict())
    user.password = make_password(user.password)
   
    try:
       user.full_clean()  # Validate the user data
       user.save()
    except Exception as e:
       return 400, {"error": str(e)}
    except Exception as e:
        return 500, {"error": "Internal server error"}

    return 201, {"ok": "User created successfully"}