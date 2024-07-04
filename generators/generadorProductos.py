import random
def generarDatosProductos():
    productos=["Música","TV","Aplicaciones","PC","Celulares","Tablets","Accesorios"]
    datos=[]
    for producto in productos:
        prodApple={}  
        categoria=random.choice(["Plus","Mega","Basic"])
        prodApple=[producto,categoria]
        datos.append(prodApple)

    return datos


print(generarDatosProductos())