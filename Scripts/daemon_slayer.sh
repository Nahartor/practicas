#!/bin/bash

DAEMON_NAME="$2"
DAEMON_PATH="$3"
DAEMON_PID="/var/run/check_reload_file.pid"

create() {
    echo "Creando el demonio ${DAEMON_NAME}"
}

start() {
    echo "Iniciando ${DAEMON_NAME}"
    ${DAEMON_PATH} &
    echo $! > ${DAEMON_PID}
}

stop() {
    echo "Deteniendo ${DAEMON_NAME}"
    kill $(cat ${DAEMON_PID})
    rm ${DAEMON_PID}
}

restart() {
    echo "Reiniciando ${DAEMON_NAME}"
    stop
    start
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    *)
        echo "Uso: $0 {start|stop|restart}"
        exit 1
        ;;
esac

exit 0
