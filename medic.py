import os.path
import csv

def load_medic():
    medicos = {}
    file_exists = os.path.isfile('./medicos.csv')

    with open('medicos.csv', 'a', newline='') as csvfile:
        headers =  ['Nombre y apellido', 'Edad', "Especialidad", "Celular", "Mail"]
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)
        print("Nombre y Apellido")
        nomvalue = str(input())
        print("Edad")
        agevalue = int(input())
        print ("Especialidad")
        espvalue = str(input())
        print ("Numero de Celular")
        numcel = str(input())
        print ("Correo Electronico")
        mail = str(input())
        medicos["Nombre y apellido"] = nomvalue 
        medicos["Edad"] = agevalue
        medicos["Especialidad"] = espvalue
        medicos["Celular"] = numcel
        medicos["Mail"] = mail 
        
        if not file_exists:
            writer.writeheader()

        writer.writerow(medicos)

import csv
def medic_array():
    with open("medicos.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print (row)
