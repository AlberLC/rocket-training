import math


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other) -> (float, 'Vector2'):
        if other is None:
            other = Vector2(1, 0)

        if type(other) is Vector2:
            return self.x * other.x + self.y * other.y
        else:
            return Vector2(self.x * other, self.y * other)

    def __rmul__(self, other) -> (float, 'Vector2'):
        return self * other

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __sub__(self, other) -> 'Vector2':
        return Vector2(self.x - other.x, self.y - other.y)

    @property
    def inverse(self) -> 'Vector2':
        return self * -1

    @property
    def module(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def normalized(self) -> 'Vector2':
        module = self.module
        return Vector2(self.x / module, self.y / module)

    def angle_deg_with(self, other: 'Vector2' = None) -> float:
        return math.degrees(self.angle_rad_with(other))

    def angle_rad_with(self, other: 'Vector2' = None) -> float:
        if other is None:
            other = Vector2(1, 0)
        angle = math.acos(self * other / (self.module * other.module))
        if self.y < 0:
            angle = 2 * math.pi - angle
        return angle

    def direccion_a(self, other) -> 'Vector2':
        return Vector2(other.x - self.x, other.y - self.y)

    def distancia_a(self, other) -> float:
        return (other - self).module

    def rotate_deg(self, angle):
        try:
            rads = math.radians(angle)
            module = self.module
            x = self.x / module
            y = self.y / module
        except ZeroDivisionError:
            return Vector2(0, 0)
        return Vector2(x * math.cos(rads) - y * math.sin(rads), x * math.sin(rads) + y * math.cos(rads)) * 20

    def rotation_deg(self) -> float:
        return math.degrees(self.rotation_rad())

    def rotation_rad(self) -> float:
        rotation = self.angle_rad_with()
        return rotation

    def validate_angle_deg_with(self, other: 'Vector2', max_angle) -> bool:
        angle = self.angle_deg_with(other)
        return angle <= max_angle or 360 - angle <= max_angle
