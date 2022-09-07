import os.path
import csv
import pandas as pd
if __name__ == '__main__': 
    print ("Bienvendo a la clinica Camila")
    entrar = input(str("Presione \n1 Si quiere ingresar al sistema \n2 Si quiere sacar un turno medico\n"))
    if entrar == "1":
        usuario = input(str("Usuario " ))
        contra = input(str("contraseña "))
        if usuario == "admin" and contra == "123":
            entrar2 = input(str("Presione \n1 Si quiere ingresar un medico sistema \n2 Si quiere ver la lista de medicos\n3 Para ver la lista de turnos\n"))
            if entrar2 == "1":
                from medic import load_medic
                load_medic ()
            elif entrar2 == "2":
                from medic import medic_array
                medic_array()
            elif entrar2 == "3":
                from patient import patient_array 
                patient_array()
        else:
            print ("Por Favor ingrese los datos de forma correcta nuevamente")
    elif entrar == "2":
        from patient import load_patient
        load_patient()  
    else:  
        print ("error, por favor ejecute de nuevo el programa")
