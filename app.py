from flask import Flask, request
import os
import psutil

app = Flask(__name__)

@app.route("/potencia")
def potencia():
    return str(2*2)

@app.route("/saludo", methods = ['POST'])
def saludo():
    if request.json: 
        nombre = request.json['nombre']
        return "hola %s"%(nombre)
    else:
        return "solicitud erronea"

@app.route("/saludo", methods = ['GET'])
def saludomundo():
    return "hola mundo"

@app.route("/totalmem")
def memtotal():
    total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    return str(total_memory)

@app.route("/percentcpu")
def percentcpu():
    return str(psutil.cpu_percent())

#
# Construya un endpoint que acepte este tipo de peticion
# curl -X POST -H "Content-type: application/json" -d '{ "comando": "ls" }' http://localhost:5000/comando
# 
# y lo que hace el endpoint es ejecutar el comando 'ls' y enviar la respuesta 
# al usuario 
#
# Tip 1: El comando os.popen() permite llevar a cabo la ejecucion de un comando 
# del sistema. Para obtener la salida por pantalla en formato cadena de 
# caracteres de lo que entrega os.popen() es necesario invocar a esa salida el
# metodo read(), de esta manera: os.popen(command).read(), donde 'command' es
#: una variable que contiene el comando que se desea ejecutar.

@app.route("/comando", methods = ['POST'])
def comando(): 
    if request.json: 
        command = request.json['command'] 
        return os.popen(command).read() 
    else: 
        return "solicitud erronea"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
