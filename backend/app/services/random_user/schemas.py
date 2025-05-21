from pydantic import BaseModel, model_validator


def _parse_user(data: dict):
    name = data.get("name", {})
    loc = data.get("location", {})
    street_info = loc.get("street", {})
    street = f"{street_info.get('name', '')} {street_info.get('number', '')}"
    city = loc.get("city", "")
    address = f"{street}, {city}".strip(", ")
    pic = data.get("picture", {}).get("large", "")

    return {
        "gender": data.get("gender", ""),
        "name": name.get("first", ""),
        "last_name": name.get("last", ""),
        "email": data.get("email", ""),
        "phone_number": data.get("phone", ""),
        "address": address,
        "photo": pic,
    }


class RandomUser(BaseModel):
    name: str
    last_name: str
    gender: str
    phone_number: str
    email: str
    address: str
    photo: str

    @model_validator(mode="before")
    def parse_model(cls, data: dict):
        return _parse_user(data)
