from datetime import datetime
from flask import Flask, request

import src.lib as lib

app = Flask(__name__)

@app.route('/')
def index():
    headers = request.headers
    forwarded_ip = headers.get('X-Forwarded-For')
    print(f"The IP address of the client is {forwarded_ip}, accessed in { datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M') }")
    lib.get_ip_info(forwarded_ip)
    return f"The IP address of the client is {forwarded_ip}"

if __name__ == '__main__':
    app.run(debug=True)
