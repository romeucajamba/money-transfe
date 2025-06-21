from ninja import NinjaAPI
from users.api import users_router

api = NinjaAPI()
api.add_router("/v1/users/", users_router)