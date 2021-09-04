# Aplicacion en Flask Contenerizada

Crear una máquina virtual a partir del [Vagrantfile](Vagrantfile) suministrado en el repositorio. 
La forma de crear la máquina virtual es a través del comando

```
vagrant up master
```

Acceden a la máquina con el comando 

```
vagrant ssh master
```

Se ubican en el directorio `/vagrant` de esta manera `cd vagrant`.

## Construcción de imagen de contenedor

Para construir la imagen ejecutan el comando:

```
docker image build -t myapp .
```

## Ejecución de la imagen de contenedor

Para ejecutar la imagen:

```
docker container run --rm -p 50000:5000 -d --name myflaskapp myapp
```

## Consumiendo servicios del contenedor

Para consumir un servicio ejecutan el comando:

```
curl http://localhost:50000/saludo
```
