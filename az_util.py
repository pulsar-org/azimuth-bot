import random, httpx


def create_session(session_type, user_id):
    print("Create a session using docker")


def get_sessions():
    return 1


def delete_session(session_id):
    print("Delete all sessions")


def gen_port():
    return int(get_sessions()) + 1


def gen_id():
    return random.randint(0, 999999)


def get_screenshot(ip, port):
    link = "https://" + ip + ":" + port + "/api/get_screenshot"
    response = httpx.post(link)
    return response