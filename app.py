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

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
