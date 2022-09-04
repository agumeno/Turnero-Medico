# Turnero-Medico-proyecto-final-
[![Whats-App-Image-2022-09-02-at-14-10-51.jpg](https://i.postimg.cc/mkGw7KMb/Whats-App-Image-2022-09-02-at-14-10-51.jpg)](https://postimg.cc/xJtM2xt7)

Este proyecto se basa en un turnero basico donde hay 2 opciones.
1. Para tener acceso a Clinica Privada Camila se debe tener usuario (admin) y contraseña (123).
  a. por medio del usuario y clave, se podra incorporar profesionales con sus correspondientes datos (Nombre y apellido,Edad,Especialidad,Celular y Mail), que estos mismos datos seran guardado en un archivo CSV
  b. En esta opcion se puede ver la lista de medicos
  c. Ver la lista de pacientes agendados con dia y hora asignados a cada profesional
2. Los pacientes podran reservar su turno con el profesional de su preferencia por medio de llamado telefonico, la secretaria debera ingresar los datos del paciente (Nombre y apellido,Edad,DNI,Celular,Mail,Medico,Dia y Hora), que tambien se guardan en otro archivo CSV, antes que ingrese con que medico quiere tener el turno se imprimira en pantalla una tabla de datos mediante la libreria PANDAS en el cual se mostraran las columnas de medicos, dia y hora del arhivo csv mencionado en este punto y 1.c para verificar que dias y horarios estan ocupados.

Dentro del repositorio podemos encontrar 3 archivos .py
1.main.py Donde se ejecuta todo el codigo principal
2.patient.py Donde estan definidas todas las funciones relacionadas con los pacientes donde luego seran importadas en main.py
3.medic.py Donde estan definidas todas las funciones relacionadas con los medicos donde luego seran importadas en main.py
