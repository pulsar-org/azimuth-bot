import httpx
import random
import os
import time
import subprocess


def get_chrome(port, id):
    return "mkdir " + id + "; cd" + id + "; sudo docker run --rm -it --shm-size=512m -p " + port + ":" + port + " -e VNC_PW=password kasmweb/chrome:1.13.0; cd .."


def get_edge(port, id):
    return "mkdir " + id + "; cd" + id + "; sudo docker run --rm -it --shm-size=512m -p " + port + ":" + port + " -e VNC_PW=password kasmweb/edge:1.13.0; cd .."


def get_brave(port, id):
    return "mkdir " + id + "; cd" + id + "; sudo docker run --rm -it --shm-size=512m -p " + port + ":" + port + " -e VNC_PW=password kasmweb/brave:1.13.0; cd .."


def get_firefox(port, id):
    return "mkdir " + id + "; cd" + id + "; sudo docker run --rm -it --shm-size=512m -p " + port + ":" + port + " -e VNC_PW=password kasmweb/firefox:1.13.0; cd .."


def get_tor(port, id):
    return "mkdir " + id + "; cd" + id + "; sudo docker run --rm -it --shm-size=512m -p " + port + ":" + port + " -e VNC_PW=password kasmweb/tor-browser:1.13.0; cd .."


def get_retroarch(port, id):
    return "mkdir " + id + "; cd" + id + "; sudo docker run --rm -it --shm-size=512m -p " + port + ":" + port + " -e VNC_PW=password kasmweb/retroarch:1.13.0; cd .."


def create_session(session_type, user_id, port, session_id):
    print("Create a session using docker")

    global process
    process = subprocess.Popen("")

    if session_type == "chrome":  # this is disgustingly bad
        process = subprocess.Popen(get_chrome(port, session_id))
    elif session_type == "edge":
        process = subprocess.Popen(get_edge(port, session_id))
    elif session_type == "brave":
        process = subprocess.Popen(get_brave(port, session_id))
    elif session_type == "firefox":
        process = subprocess.Popen(get_firefox(port, session_id))
    elif session_type == "tor":
        process = subprocess.Popen(get_tor(port, session_id))
    elif session_type == "retroarch":
        process = subprocess.Popen(get_retroarch(port, session_id))
    else:
        return

    mkdirprocess = subprocess.Popen("mkdir " + str(session_id))
    mkdirprocess.communicate()

    process.communicate()

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
