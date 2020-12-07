import dataclasses
from dataclasses import dataclass
import math

@dataclass
class Point:
    x: int
    y: int
    magnitude: float = dataclasses.field(init=False)

    def __post_init__(self):
        self.magnitude = math.sqrt(self.x**2 + self.y**2)

pythag = Point(3, 4)

print(pythag)
# Point(x=3, y=4, magnitude=5.0)