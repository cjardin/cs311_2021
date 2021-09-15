def print_it( data, state):
    print(data)

def store_json (data, state):
    print(json.dumps(data))

def store_change_data(data,state):
    print(json.dumps(data['changes']))

