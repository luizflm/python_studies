from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI()

# Simple type hint example


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


# print(get_full_name("john", "doe"))

# Type hint with Generic types example


def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


products = {
    "Orange": 5.99,
    "Coffee": 14.99,
    "Watermelon": 8.99
}

# process_items(products)


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


# say_hi('Luiz')


def alternative_say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


# alternative_say_hi()


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


person = Person("Luiz")
# print(get_person_name(person))


# Pydantic Models

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
# print(user)

# Type hints with Metadata Annotations


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"


print(say_hello("Luiz"))


@app.get("/")
def index():
    return say_hello("Luiz")
