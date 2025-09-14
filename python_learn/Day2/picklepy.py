import pickle
flight = {'flight': 'LH237', 'destination': 'Delhi', 'airline': 'Indigo'}
file_name = 'flight_info.dat'
with open(file_name, 'wb') as writer:
    pickle.dump(flight, writer)
print('Flight Info Saved Successfully.')
with open(file_name, 'rb') as reader:
    flight = pickle.load(reader)
print('data loaded from pickle file',flight)