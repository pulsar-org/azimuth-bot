import httpx
import random
import os
import time
import subprocess


def run_something(port, id, type):
    return ["mkdir", str(id) + ";", "cd", str(id) + ";", "sudo", "docker", "run", "--rm", "-it", "--shm-size=512m", "-p", str(port), ":", str(port), "-e", "VNC_PW=password", "kasmweb/" + type+"1.13.0;", "cd", ".."]

def create_session(session_type, user_id, port, session_id):
    print("Create a session using docker")

    subprocess.call(["mkdir", "session"])
    subprocess.call(["cd", "session"])

    subprocess.call(run_something(port, session_id, session_type))

    create_file(session_id, user_id, port, session_type)

    time.sleep(10)

    delete_session(session_id)


def create_file(session_id, user_id, port, session_type):
    with open(os.path.join("sessions", session_id), "x") as file:
        file.writelines("type: " + session_type + "\n" +
                        "id: " + session_id + "\n" +
                        "user_id: " + user_id + "\n" +
                        "port: " + port)
        file.close()


def get_sessions():
    return 1


def delete_session(session_id):
    path = os.path.join("sessions", session_id)
    os.remove(path)


def gen_port():
    return int(get_sessions()) + 1


def gen_id():
    return random.randint(0, 999999)


def get_screenshot(ip, port):
    link = "https://" + ip + ":" + port + "/api/get_screenshot"
    response = httpx.post(link)
    return response
