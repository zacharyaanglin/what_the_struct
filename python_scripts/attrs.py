import attr

@attr.s
class FirstQuadrantPoint():
    x = attr.ib()
    y = attr.ib()

    @x.validator
    @y.validator
    def check(self, attribute, value):
        if value <= 0:
            raise ValueError("Coordinates must be positive.")

origin = FirstQuadrantPoint(0, 0)

