#!/bin/bash

# Notificar
telegram "Start Deploy: App1-ToDo"


# Actualizar el código
git pull

# Detener el contenedor
docker compose down

# Reconstruir las imagenes que sean necesarias
docker compose up --build -d


# Verificar el código de salida
if [ $? -eq 0 ]; then
    telegram "End Deploy: App1-ToDo"

    sleep 10
    # si no esta corriendo el contenedor
    if ! docker ps | grep -q "app1"; then
        telegram "Error: App1-ToDo is not running"
    fi

else
    telegram "Error Deploy: App1-ToDo"
fi