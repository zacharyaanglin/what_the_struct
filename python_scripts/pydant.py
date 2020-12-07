from pydantic import BaseModel, ValidationError, validator

class FirstQuadrantPoint(BaseModel):
    x: int
    y: int

    @validator('x', allow_reuse=True)
    @validator('y', allow_reuse=True)
    def must_be_positive(cls, i):
        if i <= 0:
            raise ValueError('Must be positive')
        return int(i)

origin = FirstQuadrantPoint(x=1, y=1)


import datetime
from typing import List

from pydantic.dataclasses import dataclass

@dataclass
class Presentation:
    name: str
    title: str

@dataclass
class Conference:
    name: str
    time: datetime.datetime
    presentations: List[Presentation]

serialized_conference = {
        "name": "PyJamas 2020",
        "time": "2020-12-05T21:00",
        "presentations": [
            {
                "name": "Zach Anglin",
                "title": "What the struct?!",
            },
            {
                "name": "Mark Smith",
                "title": "Stupid Things I've Done with Python",
            }
        ],
    }

pyjamas = Conference(**serialized_conference)

print(pyjamas.presentations[0].title)
# What the struct?!
