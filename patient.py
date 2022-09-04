import os.path
import csv

def load_patient():
    pacientes = {}
    file_exists = os.path.isfile('./pacientes.csv')

    with open('pacientes.csv', 'a', newline='') as csvfile:
        headers =  ['Nombre y apellido', 'Edad', "DNI", "Celular", "Mail","Medico", "Dia", "Hora"]
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)
        print("Nombre y Apellido")
        nomvalue = str(input())
        print("Edad")
        agevalue = int(input())
        print ("DNI")
        espvalue = str(input())
        print ("Numero de Celular")
        numcel = str(input())
        print ("Correo Electronico")
        mail = str(input())
        watch_turn()
        print ("Medico")
        medic = str(input())
        print ("Dia de la Semana")
        dayvalue = str(input())
        print ("Hora")
        hourvalue = str(input())
        pacientes["Nombre y apellido"] = nomvalue 
        pacientes["Edad"] = agevalue
        pacientes["DNI"] = espvalue
        pacientes["Celular"] = numcel
        pacientes["Mail"] = mail 
        pacientes["Medico"] = medic
        pacientes["Dia"] = dayvalue
        pacientes["Hora"] = hourvalue 
        
        if not file_exists:
            writer.writeheader()

        writer.writerow(pacientes)

def patient_array():
    with open("pacientes.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print (row)


import pandas as pd 
def watch_turn():
    df = pd.read_csv("pacientes.csv", usecols = ["Medico" ,"Dia","Hora"])
    print(df)
