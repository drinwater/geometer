from geometer2.curve import Circle, Cone, Conic, Cylinder, Ellipse, Quadric, QuadricCollection, Sphere
from geometer2.operators import (
    angle,
    angle_bisectors,
    crossratio,
    dist,
    harmonic_set,
    is_cocircular,
    is_collinear,
    is_concurrent,
    is_coplanar,
    is_perpendicular,
)
from geometer2.point import (
    I,
    J,
    Line,
    LineCollection,
    Plane,
    PlaneCollection,
    Point,
    PointCollection,
    infty,
    infty_plane,
    join,
    meet,
)
from geometer2.shapes import (
    Cuboid,
    Polygon,
    PolygonCollection,
    Polyhedron,
    Rectangle,
    RegularPolygon,
    Segment,
    SegmentCollection,
    Simplex,
    Triangle,
)
from geometer2.transformation import (
    Transformation,
    TransformationCollection,
    affine_transform,
    identity,
    reflection,
    rotation,
    scaling,
    translation,
)
from geometer2.version import __version__
