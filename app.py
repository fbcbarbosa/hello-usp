import os
import socket
import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    name = "USP"
    hostname = socket.gethostname()
    
    html = '''
    <h1>Oi {name}!</h1>
    <h2>Hostname: {hostname}</h2>
    '''

    return html.format(name=name, hostname=hostname)

if __name__ == "__main__":
    port = 8080
    app.run(host='0.0.0.0', port=port)
