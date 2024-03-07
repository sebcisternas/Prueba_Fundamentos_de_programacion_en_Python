import requests

#funcion que obtiene datos de la api y las retorna en formato json.
def obtener_datos():
    url = 'https://aves.ninjas.cl/api/birds'
    response = requests.get(url)
    return response.json()