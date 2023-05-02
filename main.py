# this is docker don't touch this miles


import az_util
import session
import flask

app = flask.Flask("omniscient")
ip = "20.83.144.176"


@app.route('/launch/<name>', methods=['GET'])
def launch(name):
    ses = session.Session(name, 0, az_util.gen_port())
    return ip + ":" + ses.port


if __name__ == '__main__':
    app.run()
