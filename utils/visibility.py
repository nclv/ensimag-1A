import math
from typing import List

import arcade


class Block:
    def __init__(self, x: float, y: float, r: float):
        self.x = x
        self.y = y
        self.r = r

    def __repr__(self) -> str:
        return f'<Block {self.x}/{self.y}/{self.r}>'


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'<{super().__repr__()} {self.x}/{self.y}>'


class EndPoint(Point):
    begin: bool = False
    segment: 'Segment' = None
    angle: float = 0.0
    visualize: bool = False

    def __repr__(self) -> str:
        return f'<{super().__repr__()} {self.begin}/{self.angle}'


class Segment:
    p1: EndPoint
    p2: EndPoint
    d: float

    # def __repr__(self) -> str:
    #     s = f'Segment{hash(self)}'
    #     s += f'   d: {self.d}\n'
    #     s += f'   p1: {self.p1}\n'
    #     s += f'   p2: {self.p2}\n'
    #     return str(s)

    @staticmethod
    def new(p1, p2, d):
        self = Segment()
        p1.segment = self
        p1.visualize = True
        p2.segment = self
        p2.visualize = True

        self.p1 = p1
        self.p2 = p2
        self.d = d
        return self

    def __repr__(self) -> str:
        s = super().__repr__() + '\n'
        s += f'   p1: {self.p1}\n'
        s += f'   p2: {self.p2}\n'
        return str(s)


class Visibility:
    """* 2d visibility algorithm, for demo
       Usage:
          new Visibility()
       Whenever map data changes:
          loadMap
       Whenever light source changes:
          setLightLocation
       To calculate the area:
          sweep
    """

    # Construct an empty visibility set
    def __init__(self):
        # These represent the map and the light location:
        self.segments: List[Segment] = []
        self.endpoints: List[EndPoint] = []
        self.center = Point(0.0, 0.0)

        # These are currently 'open' line segments, sorted so that the nearest
        # segment is first. It's used only during the sweep algorithm, and exposed
        # as a public field here so that the demo can display it.
        self.open: List[Segment] = []

        # The output is a series of points that forms a visible area polygon
        self.output: List[Point] = []

        # For the demo, keep track of wall intersections
        self.demo_intersectionsDetected = []
        self.demo_triangle_points = []

    # Helper function to construct segments along the outside perimeter
    def _loadEdgeOfMap(self, size: int, margin: int):
        self.addSegment(margin, margin, margin, size - margin)
        self.addSegment(margin, size - margin, size - margin, size - margin)
        self.addSegment(size - margin, size - margin, size - margin, margin)
        self.addSegment(size - margin, margin, margin, margin)
        # NOTE: if using the simpler distance function (a.d < b.d)
        # then we need segments to be similarly sized, so the edge of
        # the map needs to be broken up into smaller segments.

    # Load a set of square blocks, plus any other line segments
    def loadMap(self, size: int, margin: int, blocks: List[Block], walls: List[Segment]):
        self.segments.clear()
        self.endpoints.clear()
        self._loadEdgeOfMap(size, margin)

        for block in blocks:
            x = block.x
            y = block.y
            r = block.r
            self.addSegment(x - r, y - r, x - r, y + r)
            self.addSegment(x - r, y + r, x + r, y + r)
            self.addSegment(x + r, y + r, x + r, y - r)
            self.addSegment(x + r, y - r, x - r, y - r)

        for wall in walls:
            self.addSegment(wall.p1.x, wall.p1.y, wall.p2.x, wall.p2.y)

    def addSegment(self, x1: float, y1: float, x2: float, y2: float):
        """
            Add a segment, where the first point shows up in the
            visualization but the second one does not. (Every endpoint is
            part of two segments, but we want to only show them once.)
        """
        segment = Segment()

        p1: EndPoint = EndPoint(x1, y1)
        p1.segment = segment
        p1.visualize = True

        p2: EndPoint = EndPoint(x2, y2)
        p2.segment = segment
        p2.visualize = False

        segment.p1 = p1
        segment.p2 = p2
        segment.d = 0.0

        self.segments.append(segment)
        self.endpoints.append(p1)
        self.endpoints.append(p2)

    # Set the light location. Segment and EndPoint data can't be
    # processed until the light location is known.
    def setLightLocation(self, x: float, y: float):
        self.center.x = x
        self.center.y = y

        for segment in self.segments:
            dx = 0.5 * (segment.p1.x + segment.p2.x) - x
            dy = 0.5 * (segment.p1.y + segment.p2.y) - y
            # NOTE: we only use this for comparison so we can use
            # distance squared instead of distance. However in
            # practice the sqrt is plenty fast and this doesn't
            # really help in this situation.
            segment.d = dx * dx + dy * dy

            # NOTE: future optimization: we could record the quadrant
            # and the y/x or x/y ratio, and sort by (quadrant,
            # ratio), instead of calling atan2. See
            # <https:#github.com/mikolalysenko/compare-slope> for a
            # library that does this. Alternatively, calculate the
            # angles and use bucket sort to get an O(N) sort.
            segment.p1.angle = math.atan2(segment.p1.y - y, segment.p1.x - x)
            segment.p2.angle = math.atan2(segment.p2.y - y, segment.p2.x - x)

            dAngle = segment.p2.angle - segment.p1.angle
            if dAngle <= -math.pi:
                dAngle += 2 * math.pi
            if dAngle > math.pi:
                dAngle -= 2 * math.pi
            segment.p1.begin = (dAngle > 0.0)
            segment.p2.begin = not segment.p1.begin

    # Helper: comparison function for sorting points by angle
    @staticmethod
    def _endpoint_compare(a: EndPoint, b: EndPoint) -> int:
        # Traverse in angle order
        if a.angle > b.angle:
            return 1
        if a.angle < b.angle:
            return -1
        # But for ties (common), we want Begin nodes before End nodes
        if not a.begin and b.begin:
            return 1
        if a.begin and not b.begin:
            return -1
        return 0

    @staticmethod
    def _endpoint_key(a: EndPoint) -> tuple:
        # Traverse in angle order
        return a.angle, not a.begin

    # Helper: leftOf(segment, point) returns True if point is "left"
    # of segment treated as a vector. Note that this assumes a 2D
    # coordinate system in which the Y axis grows downwards, which
    # matches common 2D graphics libraries, but is the opposite of
    # the usual convention from mathematics and in 3D graphics
    # libraries.
    @staticmethod
    def leftOf(s: Segment, p: Point) -> bool:
        # This is based on a 3d cross product, but we don't need to
        # use z coordinate inputs (they're 0), and we only need the
        # sign. If you're annoyed that cross product is only defined
        # in 3d, see "outer product" in Geometric Algebra.
        # <http:#en.wikipedia.org/wiki/Geometric_algebra>
        cross = (s.p2.x - s.p1.x) * (p.y - s.p1.y) - (s.p2.y - s.p1.y) * (p.x - s.p1.x)
        return cross < 0
        # Also note that this is the naive version of the test and
        # isn't numerically robust. See
        # <https:#github.com/mikolalysenko/robust-arithmetic> for a
        # demo of how this fails when a point is very close to the
        # line.

    # Return p*(1-f) + q*f
    @staticmethod
    def interpolate(p: Point, q: Point, f: float) -> Point:
        return Point(p.x * (1 - f) + q.x * f, p.y * (1 - f) + q.y * f)

    # Helper: do we know that segment a is in front of b?
    # Implementation not anti-symmetric (that is to say,
    # _segment_in_front_of(a, b) != (!_segment_in_front_of(b, a)).
    # Also note that it only has to work in a restricted set of cases
    # in the visibility algorithm I don't think it handles all
    # cases. See http:#www.redblobgames.com/articles/visibility/segment-sorting.html
    def _segment_in_front_of(self, a: Segment, b: Segment, relativeTo: Point) -> bool:
        # NOTE: we slightly shorten the segments so that
        # intersections of the endpoints (common) don't count as
        # intersections in this algorithm
        A1 = self.leftOf(a, self.interpolate(b.p1, b.p2, 0.01))
        A2 = self.leftOf(a, self.interpolate(b.p2, b.p1, 0.01))
        A3 = self.leftOf(a, relativeTo)
        B1 = self.leftOf(b, self.interpolate(a.p1, a.p2, 0.01))
        B2 = self.leftOf(b, self.interpolate(a.p2, a.p1, 0.01))
        B3 = self.leftOf(b, relativeTo)

        # NOTE: this algorithm is probably worthy of a short article
        # but for now, draw it on paper to see how it works. Consider
        # the line A1-A2. If both B1 and B2 are on one side and
        # relativeTo is on the other side, then A is in between the
        # viewer and B. We can do the same with B1-B2: if A1 and A2
        # are on one side, and relativeTo is on the other side, then
        # B is in between the viewer and A.
        if B1 == B2 and B2 != B3:
            return True
        if A1 == A2 and A2 == A3:
            return True
        if A1 == A2 and A2 != A3:
            return False
        if B1 == B2 and B2 == B3:
            return False

        # If A1 != A2 and B1 != B2 then we have an intersection.
        # Expose it for the GUI to show a message. A more robust
        # implementation would split segments at intersections so
        # that part of the segment is in front and part is behind.
        self.demo_intersectionsDetected.append([a.p1, a.p2, b.p1, b.p2])
        return False

        # NOTE: previous implementation was a.d < b.d. That's simpler
        # but trouble when the segments are of dissimilar sizes. If
        # you're on a grid and the segments are similarly sized, then
        # using distance will be a simpler and faster implementation.

    # Run the algorithm, sweeping over all or part of the circle to find
    # the visible area, represented as a set of triangles
    def sweep(self, maxAngle: float = 999.0):
        self.output = []  # output set of triangles
        self.demo_intersectionsDetected = []
        # TODO how to sort, solved?
        self.endpoints.sort(key=self._endpoint_key)

        self.open.clear()
        begin_angle = 0.0

        # At the beginning of the sweep we want to know which
        # segments are active. The simplest way to do this is to make
        # a pass collecting the segments, and make another pass to
        # both collect and process them. However it would be more
        # efficient to go through all the segments, figure out which
        # ones intersect the initial sweep line, and then sort them.
        for turn in range(2):
            for p in self.endpoints:
                if turn == 1 and p.angle > maxAngle:
                    # Early exit for the visualization to show the sweep process
                    break

                current_old = self.open[0] if self.open else None

                if p.begin:
                    # TODO? Insert open segment into 'open'-list but sorted
                    for i, seg in enumerate(self.open):
                        if self._segment_in_front_of(p.segment, seg, self.center):
                            continue
                        else:
                            self.open.insert(i, p.segment)
                            break
                    else:
                        self.open.append(p.segment)

                else:
                    if p.segment in self.open:
                        self.open.remove(p.segment)

                current_new = None if not self.open else self.open[0]
                if current_old != current_new:
                    if turn == 1:
                        self.addTriangle(begin_angle, p.angle, current_old)

                    begin_angle = p.angle

    def lineIntersection(self, p1: Point, p2: Point, p3: Point, p4: Point) -> Point:
        # From http://paulbourke.net/geometry/lineline2d/
        n1 = ((p4.x - p3.x) * (p1.y - p3.y) - (p4.y - p3.y) * (p1.x - p3.x))
        n2 = ((p4.y - p3.y) * (p2.x - p1.x) - (p4.x - p3.x) * (p2.y - p1.y))
        s = n1 / n2
        return Point(p1.x + s * (p2.x - p1.x), p1.y + s * (p2.y - p1.y))

    def addTriangle(self, angle1: float, angle2: float, segment: Segment):
        p1: Point = self.center
        p2: Point = Point(self.center.x + math.cos(angle1), self.center.y + math.sin(angle1))
        p3: Point = Point(0.0, 0.0)
        p4: Point = Point(0.0, 0.0)

        if segment is not None:
            # Stop the triangle at the intersecting segment
            p3.x = segment.p1.x
            p3.y = segment.p1.y
            p4.x = segment.p2.x
            p4.y = segment.p2.y
        else:
            # Stop the triangle at a fixed distance this probably is
            # not what we want, but it never gets used in the demo
            p3.x = self.center.x + math.cos(angle1)  # * 500
            p3.y = self.center.y + math.sin(angle1)  # * 500
            p4.x = self.center.x + math.cos(angle2)  # * 500
            p4.y = self.center.y + math.sin(angle2)  # * 500

        pBegin = self.lineIntersection(p3, p4, p1, p2)

        p2.x = self.center.x + math.cos(angle2)
        p2.y = self.center.y + math.sin(angle2)
        pEnd = self.lineIntersection(p3, p4, p1, p2)

        self.output.append(pBegin)
        self.output.append(pEnd)


class Dynamic(arcade.Window):

    def __init__(self):
        super().__init__(height=800)
        self.vis = Visibility()
        self.dirty = True

        self.blocks = [
            Block(200, 200, 50),
            Block(100, 200, 50),
            Block(400, 100, 50),
            Block(300, 200, 50),
            Block(300, 350, 50),
        ]
        self.walls = [
            Segment.new(EndPoint(700, 700), EndPoint(750, 750), 0.0)
        ]

        self.vis.loadMap(800, 0, self.blocks, self.walls)
        self.vis.setLightLocation(400, 400)

    def on_update(self, delta_time: float):
        if self.dirty:
            old = self.vis.output
            try:

                self.vis.sweep()
            except Exception as e:
                print(e)
                self.vis.output = old
            self.dirty = False

    def on_draw(self):
        arcade.start_render()

        ends = zip(self.vis.output[::2], self.vis.output[1::2])
        for p1, p2 in ends:
            arcade.draw_triangle_filled(
                self.vis.center.x, self.vis.center.y,
                p1.x, p1.y,
                p2.x, p2.y,
                color=(0, 100, 100)
            )

            arcade.draw_line(
                self.vis.center.x, self.vis.center.y,
                p1.x, p1.y,
                color=(168, 18, 18)
            )

            arcade.draw_line(
                self.vis.center.x, self.vis.center.y,
                p2.x, p2.y,
                color=(168, 18, 18)
            )

        for i, block in enumerate(self.blocks):
            arcade.draw_rectangle_filled(block.x, block.y, block.r * 2, block.r * 2, (255, 0, 0))
            arcade.draw_text(str(i), block.x, block.y, color=(0, 0, 0))

        for line in self.walls:
            arcade.draw_line(line.p1.x, line.p1.y, line.p2.x, line.p2.y, (0, 0, 255), 2)

        for line in self.vis.segments:
            arcade.draw_line(line.p1.x, line.p1.y, line.p2.x, line.p2.y, (0, 0, 255), 2)

        arcade.draw_circle_filled(self.vis.center.x, self.vis.center.y, 3, (242, 240, 140))

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # self.vis.setLightLocation(round(x), round(y))
        # self.dirty = True
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.vis.setLightLocation(round(x), round(y))
        self.dirty = True


if __name__ == '__main__':
    d = Dynamic()
    arcade.run()
