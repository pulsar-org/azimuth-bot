import os

import az_util
import main


class Session:
    def __init__(self, type, user_id, port):
        self.type = type
        self.user_id = user_id
        self.port = port
        self.id = az_util.gen_id()
        self.path = os.path.join("/", self.id)

        print("Creating browser type:", type, "| for user", user_id)
        az_util.create_session(type, user_id, self.port, self.id)

    def get_id(self):
        return self.id

    def destroy(self):
        az_util.delete_session(self.id)

    def screenshot(self):
        az_util.get_screenshot(main.ip, self.port)
