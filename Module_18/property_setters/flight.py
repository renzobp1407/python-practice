class flight:
    def __init__(self, segments):
        self.segments = segments



    def __repr__(self):
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)

        return ' -> '.join(stops)

    def departure_point(self):
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, val):
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val, destination=dest)

class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination
        

