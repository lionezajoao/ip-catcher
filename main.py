from flask import Flask, request

app = Flask(__name__)

@app.before_request
def get_forwarded_ip():
    headers = request.headers

    forwarded_ip = headers.get('X-Forwarded-For')
    print(forwarded_ip)

@app.route('/')
def index():
    ip_address = request.remote_addr
    return f'The IP address of the client is {ip_address}'

if __name__ == '__main__':
    app.run(debug=True)
