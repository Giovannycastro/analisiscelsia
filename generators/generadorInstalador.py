import random
def generarDatosInstaladores():
    instaladores=["Jhon doe","Pedro Perez","Ana Rubio","Carlos Zapata","Martha builes"]
    datos=[]
    for instalador in instaladores:
        responsable={}  
        edad=random.randint(25,60)
        zona=random.choice(["Zona A","Zona B","Zona C"])
        experiencia=random.randint(1,20)
        instalaciones=random.randint(20,50)
        responsable=[instalador,edad,zona,experiencia,instalaciones]
        datos.append(responsable)

    return datos


print(generarDatosInstaladores())

