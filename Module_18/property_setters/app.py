from flight import Segment, flight

seg = [Segment('EDI', 'LHR'), Segment('LHR', 'CAN')]
flight = flight(seg)

print(flight.departure_point)
print(flight)

flight.departure_point = 'GLA'
print('... Set departure to GLA...')

print(flight.departure_point)
print(flight)

