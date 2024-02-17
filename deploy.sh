#!/bin/bash

# Notificar
telegram "Start Deploy: python-course"

# Actualizar el código
git pull

# Reconstruir las imagenes que sean necesarias
docker compose up --build -d

# Notificar
telegram "End Deploy: python-course"
