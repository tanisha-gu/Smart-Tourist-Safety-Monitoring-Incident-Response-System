from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

restricted_zone = Polygon([
    (26.1, 91.1),
    (26.5, 91.1),
    (26.5, 91.5),
    (26.1, 91.5)
])


def is_inside_restricted_zone(lat, lng):
    point = Point(lat, lng)
    return restricted_zone.contains(point)
