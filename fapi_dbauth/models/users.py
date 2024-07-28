from pydantic import BaseModel, EmailStr
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: list[Event] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "fastapi@packt.com",
                "password": "Passw0rd",
                "username": "strong!!!",
                "events": [],
            }
        }
    }

class UserSingIn(BaseModel):
    email: EmailStr
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!"
            }
        }
    }
