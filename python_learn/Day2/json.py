import json
flight = {'flight': 'LH237', 'destination': 'Delhi', 'airline': 'Indigo'}
with open('flight_info.json', 'w') as writer:
    json.dump(flight, writer, indent= 4)
print('Flight Info Saved Successfully.')
with open('flight_info.json', 'r') as reader:
    flight = json.load(reader)
print('data loaded from json file',flight)
