
import requests
url = "http://localhost:8000/"
ruta_prima = url+"orders"
nueva_orden = {
    "client":"Juan Perez",
    "status":"Pendiente",
    "payment":"Tarjeta de Credito",
    "tipo":"Fisico",
    "shipping":10,
    "products":"Camiseta,Pantalon, Zapatos",

}
requests.request(method="POST",url=ruta_prima,json=nueva_orden)

nueva_orden = {
    "client":"Maria",
    "status":"Pendiente",
    "payment":"Paypal",
    "tipo":"Digital",
    "code":"ABC123",
    "expiration":"2022-12-31",

}
requests.request(method="POST",url=ruta_prima,json=nueva_orden)

response = requests.request(method="GET",url=ruta_prima)
print(response.text)
"""
ruta_estado = ruta_prima+"?status=Pendiente"
response = requests.request(method="GET",url=ruta_estado)
print(response.text)

ruta_put = ruta_prima+"/1"
actualizar = {
    
    "status":"En Proceso",
}
response = requests.request(method="PUT",url=ruta_put, json=actualizar)
print(response.text)

response = requests.request(method="GET",url=ruta_prima)
print(response.text)

ruta_eliminado = ruta_prima+"/1"
response = requests.request(method="DELETE",url=ruta_eliminado)
print(response.text)

response = requests.request(method="GET",url=ruta_prima)
print(response.text)"""