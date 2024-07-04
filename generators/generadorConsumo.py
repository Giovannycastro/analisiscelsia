import random
def generarDatos():
    datos = []
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ACH01","ACH22","ACH43"])
        marca=random.choice(["kalley","sony","rico"])
        ciudad=random.choice(["Medellin","Envigado","Sabaneta","La estrella","itagui"])
        responsable=random.choice(["Jhon doe","Pedro Perez","Ana Rubio","Carlos Zapata","Martha builes"])
        
        if ciudad == "Medellin":
            capacidad=random.randint(100,500)
            consumo=random.randint(100,500)
        elif ciudad == "Envigado":
            capacidad=random.randint(500,1000)
            consumo=random.randint(500,1000)
        elif ciudad == "Sabaneta":
            capacidad=random.randint(1000,1500)
            consumo=random.randint(1000,1500)
        elif ciudad == "La estrella":
            capacidad=random.randint(1500,2000)
            consumo=random.randint(1500,2000)
        elif ciudad=="itagui":
            capacidad=random.randint(2000,2500)
            consumo=random.randint(2000,2500)  
        dato=[id,referencia,marca,capacidad,consumo,ciudad,responsable]
        datos.append(dato)
    return datos

print(generarDatos())