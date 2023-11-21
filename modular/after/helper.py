
class Circle:

    radius: float

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius * self.radius

    def calculate_volume(self, height: float) -> float:
        return self.calculate_area() * height
