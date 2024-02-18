#!/bin/bash

THIS_PATH="/home/wecher/02-disco/01-projects/Udemy-Python-Course"
LOG_FILE="${THIS_PATH}/deploy.log"

IMAGE_NAME="python-course"
CONTAINER_NAME="web-apps"
FULL_NAME="${IMAGE_NAME}:${CONTAINER_NAME}"


my-echo(){
    ############################################
    ############### LOG COLUMNS ################
    ####### Date,Time,Status,Description #######
    ############################################
    echo "$(date -I),$(date +"%T"),$1,$2" >> "${LOG_FILE}"
    telegram "$1: $2"
}



# Voy a la carpeta del proyecto
cd "${THIS_PATH}"

# Notificar
my-echo "OK" "Deploy start ${FULL_NAME}"

# Actualizar el código
git pull

# Reconstruir las imagenes que sean necesarias
docker compose up --build --detach

# Notificar
my-echo "OK" "Deploy end ${FULL_NAME}"

