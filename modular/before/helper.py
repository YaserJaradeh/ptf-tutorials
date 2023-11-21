def calculate_area(radius: float) -> float:
    return 3.14 * radius * radius


def calculate_volume_bad(radius: float, height: float) -> float:
    return 3.14 * radius * radius * height


def calculate_volume_ok(area: float, height: float) -> float:
    return area * height
