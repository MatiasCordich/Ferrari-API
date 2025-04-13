import json

# Función para cargar los datos de ferraris.json
def cargar_ferraris():
    with open('./data/ferraris.json', 'r') as f:
        return json.load(f)