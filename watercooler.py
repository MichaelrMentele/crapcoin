#!/usr/bin/env python3
"""
Manage nodes.
- start nodes
- kill nodes

watercooler -x fullnodes
"""
import sys
import subprocess
import time


def run_bash(cmd):
    subprocess.call(['bash', '-c', cmd])


def kill_on_port(port):
    print("Cleaning up port: %s" % port)
    try:
        cmd = "fuser -k -n tcp %s" % port
        run_bash(cmd)
    except FileNotFoundError:
        # Port is already clean
        pass


def kill_docker_containers():
    print("Stopping and killing all containers...")
    stop_cmd = "sudo docker stop $(sudo docker ps -a -q)"
    run_bash(stop_cmd)
    rm_cmd = "sudo docker rm $(sudo docker ps -a -q)"
    run_bash(rm_cmd)


def start_fullnode(port):
    # cmd = "python manage.py runserver %s &" % (port)
    cmd = ("sudo docker-compose run -de PORT={port} "
           "web /app/start.sh").format(port=port)
    print("starting node listening at port: %s" % port)
    run_bash(cmd)


def start_sauron(port=None):
    port = port or 8999
    cmd = ("sudo docker-compose run -d -e PORT={port} "
           "sauron /app/start.sh").format(port=port)
    print("Starting up Sauron")
    run_bash(cmd)


if __name__ == "__main__":
    args = sys.argv
    nodes = args[1]

    kill_docker_containers()
    for n in range(0, int(nodes)):
        port = 8000 + n
        start_fullnode(port)
        time.sleep(1)

    start_sauron()
